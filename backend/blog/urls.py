
from django.contrib import admin
from django.urls import path, include
from posts.views import PostView, TagView, PostByTagView
from core.views import AuthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', AuthView.as_view()),
    path(
        'api/posts/',
        PostView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_post_create_list',
    ),
    path(
        'api/post/<int:pk>/',
        PostView.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            },
        ),
        name='api_post_get_put_path_delete',
    ),
    path(
        'api/tags/',
        TagView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_tag_create_list',
    ),
    path(
        'api/tag/<int:pk>/',
        TagView.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            },
        ),
        name='api_tag_get_put_path_delete',
    ),
    path(
        'api/tag/<int:pk>/posts',
        PostByTagView.as_view(
            {
                'get': 'list',
            },
        ),
        name='api_post_by_tag',
    ),
    path('api-auth/', include('rest_framework.urls')),
]
