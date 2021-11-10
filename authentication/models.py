from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Логин', default='empty',max_length=100)
    email = models.EmailField('Почта', unique=True, max_length=100)
    password = models.CharField('Пароль', max_length=300)
    is_staff = models.BooleanField('Сотрудник?', default=False)
    is_superuser = models.BooleanField('Суперпользователь?', default=False)
    last_login = models.DateTimeField('Время последнего входа', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ['email']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
