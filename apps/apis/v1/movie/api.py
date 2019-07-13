from rest_framework.viewsets import ModelViewSet

from .serializers import MovieModelSerializer
from apps.movie.models import Movie


class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerializer
    queryset = Movie.objects.all()
