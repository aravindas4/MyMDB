from rest_framework import serializers

from apps.user.models import User


class UserModelSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'password', 'email')

    def create(self, validated_data):
        validated_data['username'] = validated_data.get('email')
        return super().create(validated_data)
