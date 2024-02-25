from django.contrib.auth.models import AbstractUser
from django.db import models

from chain.models import NULLABLE
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField

class UserRoles(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'


class User(AbstractUser):
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = PhoneNumberField(max_length=100, verbose_name='Номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    image = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
