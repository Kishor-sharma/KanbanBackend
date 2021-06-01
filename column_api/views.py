from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication, serializers, status
from django.contrib.auth.models import User
from .models import Lanes
from .serializer import LanesSerializer

# Create your views here.
class LaneAPIView(APIView):
    def get(self, request):
        column = Lanes.objects.all()
        serializer = LanesSerializer(column, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LanesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaneDetailView(APIView):
    def get_object(self, pk):
        try:
            return Lanes.objects.get(pk=pk)
        except Lanes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        column = self.get_object(pk)
        serializer = LanesSerializer(column)
        return Response(serializer.data)

    def put(self, request, pk):
        column = self.get_object(pk)
        serializer = LanesSerializer(column, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        column = self.get_object(pk)
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)