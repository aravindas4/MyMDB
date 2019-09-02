from django.urls import path, include
from .api import LoginAPI, LogoutAPI, UserModelViewSet

from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
]

router = SimpleRouter()
router.register('', UserModelViewSet, basename='user')

urlpatterns += router.urls