from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/products/', include('products.urls')),
]
