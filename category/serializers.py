from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent',)

    # Переопределяем метод to_representation для вывода подкатегорий
    def to_representation(self, instance):
        representation = super().to_representation(instance)  # сперва мы вызваем родительскую логикуа потом только
        # переопределяыем данную функцию

        # делаем проверку, есть или нет подкатегории
        if instance.children.exists():
            # тут у нас рекурсия которая вызвает сама себя каждый раз и подставляет категорию чилдрен
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation
