from django.urls import path

from rest_framework.routers import SimpleRouter

from .api import (MovieModelViewSet, PersonModelViewSet, VoteModelViewSet)

router = SimpleRouter()
router.register('person', PersonModelViewSet, basename='movie-person')
router.register('vote', VoteModelViewSet, basename='movie-vote')
router.register('', MovieModelViewSet, basename='movie')

urlpatterns = router.urls
