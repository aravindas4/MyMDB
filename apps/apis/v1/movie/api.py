from django.db.models import Prefetch

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import (MovieModelSerializer, PersonDetailSerializer,
                          PersonListSerialiazer, MovieDetailSerializer,
                          VoteSerializer)
from apps.movie.models import (Movie, Person, MoviePerson, MovieImage, Vote)


class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerializer
    queryset = Movie.objects.prefetch_related(
                Prefetch(
                    'vote_set',
                    queryset=Vote.objects.select_related('user')
                )
            )

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return MovieDetailSerializer
        return self.serializer_class


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
            # return self.queryset
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonListSerialiazer
        return self.serializer_class


class VoteModelViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data['movie'] = instance.movie.id
        request.data['user'] = request.user.id
        return super().update(request, *args, **kwargs)