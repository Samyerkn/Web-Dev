# api/serializers.py

from rest_framework import serializers
from .models import Company, Vacancy

# ModelSerializer для Company
class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Serializer для Vacancy
class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = serializers.IntegerField()

    def create(self, validated_data):
        return Vacancy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
