from django.db import models
from rest_framework import serializers
from .models import Lanes

class LanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lanes
        fields = ['id', 'name', 'index']