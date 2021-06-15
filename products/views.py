from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from . import serializers
from .models import Product


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class =  serializers.ProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = StandardResultsSetPagination # чтобы разбить по страницам