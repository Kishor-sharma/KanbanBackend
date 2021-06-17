from column_api import serializer
from django.db.models import fields
from rest_framework import serializers
from .models import BoardColumn

class BoardColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardColumn
        fields = ['id', 'capacity', 'limit', 'board_id', 'column_id']