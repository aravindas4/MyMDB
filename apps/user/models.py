from django.db import models

from django.contrib.auth.models import AbstractUser

# from token.models import Multitoken


class User(AbstractUser):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.username}'

    def get_auth_token(self):
        return