from django.contrib.auth import login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import status, response, permissions, viewsets
from .serializers import UserModelSerializer
from apps.user.models import User
from rest_framework.decorators import action


class LoginAPI(APIView):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        data = {
            'name': user.first_name,
            'email': user.email,
            'photograph': user.photograph,
            'token': user.get_auth_token()
        }
        return response.Response(data, status=status.HTTP_200_OK)


class LogoutAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.user.delete_auth_token(key=request.auth)
        logout(request)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=True, url_path='change-details')
    def change_details(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
