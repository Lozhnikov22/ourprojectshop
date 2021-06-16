from rest_framework import serializers


from products.models import Product, ProductImages
from comments.serializers import FeedbackSerializer
from products.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # print(validated_data)
        request = self.context.get('request')
        # print("Файлы: ", request.FILES)
        images_data = request.FILES
        created_product = Product.objects.create(**validated_data)
        print(created_product)
        print("Work", images_data.getlist('image'))
        print("is not work: ", images_data)
        # for image_data in images_data.getlist('images'):
        #     PostImages.objects.create(post=created_post, image=image_data)
        images_obj = [
            ProductImages(product=created_product, image=image) for image in images_data.getlist('image')
        ]
        ProductImages.objects.bulk_create(images_obj)
        return created_product

    def to_representation(self, instance):  # он отвечает за то в каком виде возвращается Response
        representation = super().to_representation(
            instance)  # подтягиваем родительский метод и добавляем свою переменную
        #  и так в instance  сейчас хранится Post,  чтобы вытащить все картинки этого поста
        # мы можем обратиться через related_name = 'images'  типа Post.images.all()

        representation['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation2['feedbacks'] = FeedbackSerializer(instance.feedbacks.all(), many=True, context=self.context).data
        return representation, representation2


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

