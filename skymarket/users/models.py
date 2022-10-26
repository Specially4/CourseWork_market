from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор')
    )
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=12, validators=[MinValueValidator(limit_value=11, message='Invalid phone number')])
    email = models.EmailField(unique=True)
    role = models.CharField(choices=UserRoles.choices, default='user', max_length=13)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
