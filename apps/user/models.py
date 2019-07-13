from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from ordered_model.models import OrderedModel
from tokens.models import MultiToken
from apps.utils.models import Base
from apps.utils import const

from model_utils import Choices


class User(AbstractUser):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.username}'

    def get_auth_token(self):
        return "Token " + MultiToken.objects.create(user_id=self.id).key

    def delete_auth_token(self, key):
        MultiToken.objects.filter(key=key).delete()

    def logout(self):
        MultiToken.objects.filter(user_id=self.id).delete()
