from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ourshopmarket.views import ProductImageViewSet

router = routers.SimpleRouter()
router.register('post_images', ProductImageViewSet)


urlpatterns = [
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/categories/', include('category.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/products/like/', include('like.urls')),
    path('api/v1/feedbacks/', include('comments.urls')),
]
