from rest_framework import serializers
from . import models
from .models import kinds
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animals
        fields = "__all__"


class CagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cages
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ["id", "age", "position", "name", "surname"]

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("You can't employ an underaged person")
        else:
            return value


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Positions
        fields = "__all__"

    def validate_wage(self, value):
        if value < 7.25:
            raise serializers.ValidationError("Minimum wage is $7.25")
        else:
            return value


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
