from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор')
    )


class User(AbstractBaseUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = UserManager()

    first_name = models.CharField(
        max_length=64,
        verbose_name='Имя',
        help_text='Введите ваше имя, макс 64 символов'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='Фамилия',
        help_text='Введите вашу фамилию, макс 64 символов'
    )
    phone = PhoneNumberField()
    email = models.EmailField(verbose_name='email address', unique=True, help_text='Введите вашу электронную почту')
    role = models.CharField(
        choices=UserRoles.choices,
        max_length=13,
        verbose_name='Роль пользователя',
        help_text='Выберите роль'
    )
    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        verbose_name='',
        help_text='Загрузите изображение'
    )
    is_active = models.BooleanField(default=False)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_modul_perm(self, app):
        return self.is_admin