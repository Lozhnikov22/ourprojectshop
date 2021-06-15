from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
# ереводчик языка
from django.utils.translation import gettext_lazy as _


# Делаем регистрацию по почте, переписываем встроенный менеджер
class UserManager(BaseUserManager):
    use_in_migrations = True  # при определении базавого метода регестрации, необходимо сделать миграцию

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()  # вызываем функцию которая вызывает активацию кода
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError("Super user must have status is_staff=True")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Super user must have status is_superuser=True")
        return self._create_user(email, password, **kwargs)


class CustomUser(AbstractUser):
    password = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=40, blank=True)
    objects = UserManager()  # переопределили на наш менеджер который написали выше
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField('Email address', unique=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email' # указываем что активация будет через почту
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # Метод для активационного кода
    def create_activation_code(self):
        import uuid  # это генератор ключей
        code = str(uuid.uuid4())  # выбираем какой генератор использовать, можно посмотреть чеерз контрл
        self.activation_code = code  # записываем код к юзеру

    # Проверяем активатион код
    def activate_with_code(self, code):
        if str(self.activation_code) != str(code):
            raise Exception('Code is invalid')
        self.is_active = True  # Делаем Юзера активным
        self.activation_code = ''  # очищаем активационный код, после проверки.
        self.save(update_fields=['is_active', 'activation_code'])  # мы сохраняем поля, и указываем какие поля сохранить
