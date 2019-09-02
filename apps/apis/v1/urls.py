from django.urls import include, path

from .movie import urls as movie_url
from .user import urls as user_url

urlpatterns = [
    path('movie/', include(movie_url)),
    path('user/', include(user_url))
]