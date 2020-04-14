from rest_framework import serializers
from v1.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'date_created', 'last_login', 'is_active', 'password']