from django.urls import path

from rest_framework.routers import SimpleRouter

from .api import MovieModelViewSet

router = SimpleRouter()
router.register('', MovieModelViewSet, basename='movie')

urlpatterns = router.urls
