from django.db import models

from django.utils.translation import gettext as _
from ordered_model.models import OrderedModel
from apps.utils.models import Base
from apps.utils import const

from model_utils import Choices

from apps.user.models import User


class Movie(Base):
    RATING_TYPE = Choices(
        const.NOT_RATED,
        const.RATED_G,
        const.RATED_PG,
        const.RATED_R
    )

    title = models.CharField(_('title'), max_length=255)
    plot = models.TextField(_('plot'), blank=True)
    date = models.DateField(_('release date'), null=True, blank=True)
    runtime = models.PositiveSmallIntegerField(_('runtime in mins'),
                                               null=True, blank=True)
    website = models.URLField(_('website'), null=True, blank=True)
    rating = models.PositiveSmallIntegerField(_('rating'),
                                              choices=RATING_TYPE)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        if self.date:
            return f'{self.title} ({self.date.year})'
        else:
            return f'{self.title}'


class MovieImage(Base, OrderedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    path = models.CharField(_('image path'), max_length=255)

    order_with_respect_to = 'movie'

    class Meta:
        verbose_name = 'Movie Image'
        verbose_name_plural = 'Movie Images'

    def __str__(self):
        return f'{self.movie}: {self.path}'


class Person(Base):
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    died_on = models.DateField(_('died on'), null=True, blank=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str(self):
        return f'{self.first_name} {self.last_name}'


class MoviePerson(Base):
    ROLE = Choices(
        const.ACTOR,
        const.DIRECTOR,
        const.WRITER
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.PositiveIntegerField(_('role'), choices=ROLE, blank=True,
                                       null=True)
    detail = models.CharField(_('role detail'), null=True, blank=True,
                              max_length=255)

    class Meta:
        verbose_name = 'Movie Person'
        verbose_name_plural = 'Movie Persons'


class Vote(Base):
    VOTE_TYPE = Choices(
        const.VOTE_UP,
        const.VOTE_DOWN
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.PositiveSmallIntegerField(_('Vote'), choices=VOTE_TYPE,
                                            null=True)

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'

    def __str__(self):
        return f'{self.user}: {self.movie} - {self.vote}'
