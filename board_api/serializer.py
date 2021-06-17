from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name']

class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name']