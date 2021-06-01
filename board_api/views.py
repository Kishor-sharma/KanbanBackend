from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from board_api.serializer import BoardSerializer, BoardDetailSerializer
from .models import Board

# Create your views here.
class BoardAPIView(APIView):
    def get(self, request):
        board = Board.objects.all()
        serializer = BoardDetailSerializer(board, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        print("This is serializer: ", serializer)
        print("This is user Detail: ", request.user, "and the id is: ", request.user.id)

        if serializer.is_valid():
            serializer.save(userID=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailView(APIView):
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardDetailSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)