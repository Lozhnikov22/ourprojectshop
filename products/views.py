from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from . import serializers
from .models import Product, ProductImages
from .serializers import ProductImageSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = StandardResultsSetPagination  # чтобы разбить по страницам


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductImageView(generics.ListAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductFilterView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
                Q(title__icontains=query) | Q(price__icontains=query)
            )
        return object_list

