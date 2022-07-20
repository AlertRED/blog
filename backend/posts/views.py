from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Post, Tag
from .serializers import (
    PostSerializer,
    PostsByTagSerializer,
    TagSerializer,
)


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def add_tag(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=self.kwargs['tag_pk'])
        post: Post = self.get_object()
        if tag in post.tags.all():
            raise ValidationError('Пост уже содержит тег')
        post.tags.add(tag.id)
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostByTagView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = PostsByTagSerializer

    def get_queryset(self):
        return Post.objects.filter(
            tags__id=self.kwargs.get('pk'),
        ).order_by('-created')
