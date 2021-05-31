from django.db.models import fields
from rest_framework import serializers
from .models import BoardColumn

class BoardColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardColumn
        fields = ['boardID', 'columnID', 'capacity', 'limit']