from rest_framework import serializers

from products.models import Product

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'likes', 'dislikes')