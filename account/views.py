from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from account.send_mail import send_confirmation_email
from . import serializers

User = get_user_model()


class RegisterApiView(APIView):
    # переопределяем метод пост
    def post(self, request):
        serializer = serializers.RegisterApiSerializer(data=request.data)  # где в дате отправляем два пароля и емаил
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()  # при вызове save под капотом вызовится create(который мы прописали в
            # сериазаторе) и создаст юзера

            # тут мы отправляем письмо используя нашу созданную функцию:
            if user:
                send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)  # проверяем код
            user.is_active = True  # говорим что юзер теперь активынй
            user.activation_code = ''  # удаляем активационный код
            user.save()
            # в Response  передаем json
            return Response({'msg': 'Successfully activated'}, status=status.HTTP_200_OK)
        # если он второй раз перейдет по той ссылке котороую мы егму отправили то выйдет ниже прописанное
        except User.DoesNotExist:
            return Response({'msg': 'Link expired'}, status=status.HTTP_201_CREATED)


# JWT настройка
class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer


