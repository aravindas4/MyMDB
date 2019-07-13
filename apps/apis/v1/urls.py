from django.urls import include, path

from .movie import urls as movie_url

urlpatterns = [
    path('movie/', include(movie_url)),
]