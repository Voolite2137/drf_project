from rest_framework import serializers
from . import models
from .models import kinds

class AnimalsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    kind = serializers.ChoiceField(choices=kinds)
    name = serializers.CharField(max_length = 100)
    additionalInfo = serializers.CharField(max_length=300)
    cage = serializers.PrimaryKeyRelatedField(queryset = models.Cages.objects.all())
    
    def create(self,validated_data):
        return models.Animals(**validated_data)

    def validate(self,data):
        if data['name']=='nigger':
            raise serializers.ValidationError("Co ty rasisto")
        else:
            return data

class CagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cages
        fields = '__all__'

    

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ['id','age','position','name','surname']

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Positions
        fields = '__all__'

