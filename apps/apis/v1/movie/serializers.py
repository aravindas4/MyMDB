from rest_framework import serializers

from apps.movie import models
from apps.utils.serializers import ChoicesField


class MovieModelSerializer(serializers.ModelSerializer):
    rating = ChoicesField(choices=models.Movie.RATING_TYPE)

    class Meta:
        model = models.Movie
        fields = ('id', 'name', 'plot', 'rating')


class MoviePersonModelSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source='movie.name')
    movie_id = serializers.CharField(source='movie.id')
    role = ChoicesField(choices=models.MoviePerson.ROLE)

    class Meta:
        model = models.MoviePerson
        fields = ('movie_name', 'role', 'movie_id')


class PersonListSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = ('id', 'name')


class PersonDetailSerializer(serializers.ModelSerializer):
    actor = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    writer = serializers.SerializerMethodField()

    class Meta:
        model = models.Person
        fields = ('id', 'name', 'date_of_birth', 'died_on', 'actor',
                  'director', 'writer')

    def get_actor(self, obj):
        return MoviePersonModelSerializer(obj.movieperson_set.actors(),
                                          many=True).data

    def get_director(self, obj):
        return MoviePersonModelSerializer(obj.movieperson_set.directors(),
                                          many=True).data

    def get_writer(self, obj):
        return MoviePersonModelSerializer(obj.movieperson_set.writers(),
                                          many=True).data
