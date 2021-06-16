from rest_framework import serializers

from comments.serializers import FeedbackSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):  # он отвечает за то в каком виде возвращается Response
        representation = super().to_representation(
            instance)  # подтягиваем родительский метод и добавляем свою переменную
        #  и так в instance  сейчас хранится Post,  чтобы вытащить все картинки этого поста
        # мы можем обратиться через related_name = 'images'  типа Post.images.all()
        representation['feedbacks'] = FeedbackSerializer(instance.feedbacks.all(), many=True, context=self.context).data
        return representation
