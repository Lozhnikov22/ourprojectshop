from rest_framework import mixins, viewsets

from products import serializers
from products.models import ProductImages


class ProductImageViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = ProductImages.objects.all()
