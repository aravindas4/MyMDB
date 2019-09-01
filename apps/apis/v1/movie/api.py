from django.db.models import Prefetch

from rest_framework.viewsets import ModelViewSet

from .serializers import MovieModelSerializer, PersonDetailSerializer, \
    PersonListSerialiazer
from apps.movie.models import Movie, Person, MoviePerson, MovieImage, Vote


class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerializer
    queryset = Movie.objects.prefetch_related(
        Prefetch(
            'movieimage_set',
            queryset=MovieImage.objects.select_related('user')
        )
    )


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return self.queryset.prefetch_related(
                Prefetch(
                    'movieperson_set',
                    queryset=MoviePerson.objects.select_related('movie')\
                        .prefetch_related(
                        Prefetch(
                            'movie__movieimage_set',
                            queryset=MovieImage.objects.select_related('user')
                        ), Prefetch(
                            'movie__vote_set',
                            queryset=Vote.objects.select_related('user')
                        )
                    )
                )
            )
            # return self.queryset
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonListSerialiazer
        return self.serializer_class
