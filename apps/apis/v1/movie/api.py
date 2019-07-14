from django.db.models import Prefetch

from rest_framework.viewsets import ModelViewSet

from .serializers import MovieModelSerializer, PersonDetailSerializer, \
    PersonListSerialiazer
from apps.movie.models import Movie, Person, MoviePerson


class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerializer
    queryset = Movie.objects.all()


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return self.queryset.prefetch_related(
                Prefetch(
                    'movieperson_set',
                    queryset=MoviePerson.objects.select_related('movie')
                )
            )
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonListSerialiazer
        return self.serializer_class
