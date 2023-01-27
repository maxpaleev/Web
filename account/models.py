from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, help_text='Ваша почта')
    username = models.CharField(_('username'), max_length=50, unique=True, help_text='Ваш логин')
    first_name = models.CharField(_('first name'), max_length=30, blank=False, help_text='Ваше имя')
    last_name = models.CharField(_('last name'), max_length=30, blank=False, help_text='Ваша фамилия')
    # password = models.CharField(_('password'), max_length=20, blank=True, help_text='Ваш пароль')
    # is_active = models.BooleanField(_('active'), default=True)
    is_superuser=models.BooleanField(_('superuser'), default=False)
    is_staff=models.BooleanField(_('staff'), default=False)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
