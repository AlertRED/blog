from django.contrib import admin
from drf_yasg.views import get_schema_view
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from rest_framework import permissions

from contact.views import ContactView
from post.views import (
    FilePostCreateView,
    FilePostGetView,
    PostView,
    CategoryView,
    PostByCategoryView,
)
from core.views import AuthView, KeyValueView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    re_path('admin/', admin.site.urls),
    re_path('api/auth/login/', AuthView.as_view()),
    re_path(
        'api/posts/',
        PostView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_post_create_list',
    ),
    re_path(
        'api/post/(?P<pk>[0-9A-Fa-f-]+)/',
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
    re_path(
        'api/categories/',
        CategoryView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_category_create_list',
    ),
    re_path(
        'api/category/(?P<pk>[0-9A-Fa-f-]+)/',
        CategoryView.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            },
        ),
        name='api_category_get_put_patch_delete',
    ),
    re_path(
        'api/category/(?P<pk>[0-9A-Fa-f-]+)/posts',
        PostByCategoryView.as_view(
            {
                'get': 'list',
            },
        ),
        name='api_post_by_category',
    ),
    re_path(
        'api/key-values/',
        KeyValueView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_key_value_create_list',
    ),
    re_path(
        'api/key-value/(?P<pk>[0-9A-Fa-f-]+)/',
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
    re_path(
        'api/contacts/',
        ContactView.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='api_contact_create_list',
    ),
    re_path(
        'api/contact/(?P<pk>[0-9A-Fa-f-]+)/',
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
    re_path('api-auth/', include('rest_framework.urls')),
    re_path(
        'api/post-files/',
        FilePostCreateView.as_view(),
        name='api_post_file_create',
    ),
    re_path(
        'api/post-file/(?P<pk>[0-9A-Fa-f-]+)/',
        FilePostGetView.as_view(),
        name='api_post_file_get',
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
