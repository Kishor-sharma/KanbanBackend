from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, authentication, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
from board_api.models import Board
from column_api.models import Lanes

# Create your views here.
class TaskAPIView(APIView):
    def get_specificTask(self, boardID=None, columnID=None):
        queryset = Task.objects.all()
        if boardID:
            print("got boardID")
            queryset = queryset.filter(boardID=boardID)
        if columnID:
            queryset = queryset.filter(columnID=columnID)

        serializer = TaskSerializer(queryset, many=True)
        return serializer.data

    def get(self, request, boardID=None, columnID=None): #, , columnID=None
        print('Hello man: ', boardID, columnID)
        tasks = self.get_specificTask(boardID, columnID)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        board_exist = Board.objects.filter(id=request.data['boardID']).exists()
        lane_exist = Lanes.objects.filter(id=request.data['columnID']).exists()

        if board_exist and lane_exist:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class TaskDetailView(APIView):
    def check_boardcolumn(self, boardID, columnID):
        board_exist = Board.objects.filter(id=boardID).exists()
        lane_exist = Lanes.objects.filter(id=columnID).exists()
        return board_exist and lane_exist

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        task = self.get_object(pk)
        if isinstance(task, Response):
            return task
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        if not self.check_boardcolumn(request.data['boardID'], request.data['columnID']):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        task = self.get_object(pk)
        if isinstance(task, Response):
            return task
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        if not self.check_boardcolumn(request.data['boardID'], request.data['columnID']):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        task = self.get_object(pk)
        if isinstance(task, Response):
            return task
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)