from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()  # это базовый класс юзера орентируется на auth.User


class RegisterApiSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)  # не нужен для вывода, поэтому

    # write_only=True, required=True - говорит что поле обьязательное

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    # Переопределяем метод валидейт, чтоб он проверял 2 пароля
    def validate(self, attrs):
        password2 = attrs.pop('password2')  # удаляем пароль 2
        if attrs.get('password') != password2:
            raise serializers.ValidationError("Password and Password2 did not match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# при логине юзера мы хотим выдать юзеру JWT token поэтому пишем данный сериализатор
class LoginSerializer(TokenObtainPairSerializer):
    # получаем пароль от юзера, емаил не указываем потому что под капотом уже получаем его
    password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.pop('password', None)
        # если exists вытащит False то мы ему выдаем ошибку
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found')
        # authenticate уже встроенная функция для авторизациии которая принимает емаил и пароль
        user = authenticate(username=email, password=password)
        # если юзеар активный и он авторизавался то мы даем ему токен
        if user and user.is_active:
            refresh = self.get_token(user)
            # refresh  надо передавать обязательно! Нужен для обновления токена
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)
        return attrs
