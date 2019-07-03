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


class Vote(Base, OrderedModel):
    VOTE_TYPE = Choices(
        const.VOTE_UP,
        const.VOTE_DOWN
    )
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.PositiveSmallIntegerField(_('Vote'), choices=VOTE_TYPE,
                                            null=True)

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'

    def __str__(self):
        return f'{self.user}: {self.movie} - {self.vote}'
