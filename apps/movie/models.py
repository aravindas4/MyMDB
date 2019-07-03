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
    date = models.DateField(_('date'), null=True, blank=True)
    runtime = models.PositiveSmallIntegerField(_('runtime in mins'),
                                               null=True, blank=True)
    webiste = models.URLField(_('webiste'), null=True, blank=True)
    rating = models.PositiveSmallIntegerField(_('rating'),
                                              choices=RATING_TYPE,
                                              )

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.title} ({self.date.year})'


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

    class Meta:
        verbose_name = 'Movie Person'
        verbose_name_plural = 'Movie Persons'
