from rest_framework import serializers
from .models import TodoModel
from django.contrib.auth.models import User


class TodoSer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model = TodoModel
        fields="__all__"

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','password','email']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)