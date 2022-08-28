from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import filters
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .pagination import PostPagination, CategoryPagination
from .filters import PostFilter
from .models import Post, Category, PostFile
from .serializers import (
    FileCreateSerializer,
    FileGetSerializer,
    PostSerializer,
    CategorySerializer,
)


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['title']
    ordering_fields = ['created']
    filterset_class = PostFilter
    pagination_class = PostPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        return Post.objects.filter(is_draft=False)


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CategoryPagination


class PostByCategoryView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            category__id=self.kwargs.get('pk'),
        ).order_by('-created')


class FilePostCreateView(CreateAPIView):
    """"""
    queryset = PostFile.objects.all()
    serializer_class = FileCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance = serializer.save()
        return Response(FileGetSerializer(instance).data)


class FilePostGetView(RetrieveAPIView):
    """"""
    queryset = PostFile.objects.all()
    serializer_class = FileGetSerializer
