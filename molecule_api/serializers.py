from dataclasses import field
from rest_framework import serializers
from .models import MoleculeApi

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoleculeApi
        fields = '__all__'