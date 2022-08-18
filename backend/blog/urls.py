from django.contrib import admin
from django.urls import path, include

from contact.views import ContactView
from post.views import PostView, TagView, PostByTagView
from core.views import AuthView, KeyValueView

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
        name='api_post_get_put_patch_delete',
    ),
    path(
        'api/post/<int:pk>/add-tag/<int:tag_pk>/',
        PostView.as_view({
            'put': 'add_tag',
        }),
        name='api_add_tags',
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
        name='api_tag_get_put_patch_delete',
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
    path(
        'api/key-value/',
        KeyValueView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_key_value_create_list',
    ),
    path(
        'api/key-value/<int:pk>/',
        KeyValueView.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            },
        ),
        name='api_key_value_get_put_patch_delete',
    ),
    path(
        'api/contact/',
        ContactView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_contact_create_list',
    ),
    path(
        'api/contact/<int:pk>/',
        ContactView.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            },
        ),
        name='api_contact_get_put_patch_delete',
    ),
    path('api-auth/', include('rest_framework.urls')),
]
