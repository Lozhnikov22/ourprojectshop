from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ourshopmarket.views import ProductImageViewSet

schema_view = get_schema_view(
    info=openapi.Info(
        title='OurShop project',
        default_version='v1',
        description='this is our shop project',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='test@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = routers.SimpleRouter()
router.register('post_images', ProductImageViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/categories/', include('category.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/products/like/', include('like.urls')),
    path('api/v1/feedbacks/', include('comments.urls')),
    path('api/v1/cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)