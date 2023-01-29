from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# from django.utils.translation import ugettext_lazy as _


from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Логин',
                                max_length=255,
                                unique=True
                                )
    first_name = models.CharField(verbose_name='Имя',
                                  max_length=255,
                                  unique=True,
                                  blank=False,
                                  )
    last_name = models.CharField(verbose_name='Фамилия',
                                 max_length=255,
                                 unique=True,
                                 blank=False,
                                 )
    email = models.EmailField(verbose_name='Почта',
                              null=True,
                              blank=True
                              )

    is_active = models.BooleanField(verbose_name='active',
                                    default=False
                                    )
    is_staff = models.BooleanField(verbose_name='staff',
                                   default=False
                                   )
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        unique_together = ['username']

    def __str__(self):
        return self.username
