from rest_framework import serializers

from apps.movie import models
from apps.utils.serializers import ChoicesField


class MovieModelSerializer(serializers.ModelSerializer):
    rating = ChoicesField(choices=models.Movie.RATING_TYPE)

    class Meta:
        model = models.Movie
        fields = ('id', 'name', 'plot', 'rating')
