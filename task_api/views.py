from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
from board_api.models import Board
from column_api.models import Lanes

# Create your views here.
class TaskAPIView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_specificTask(self, board_id=None, column_id=None):
        queryset = Task.objects.all()
        if board_id:
            queryset = queryset.filter(board__pk=board_id)
        if column_id:
            queryset = queryset.filter(column__pk=column_id)

        serializer = TaskSerializer(queryset, many=True)
        return serializer.data

    def get(self, request, board_id=None, column_id=None):
        tasks = self.get_specificTask(board_id, column_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        board = Board.objects.filter(pk=request.data['board_id'])
        lane = Lanes.objects.filter(pk=request.data['column_id'])

        if not (board.exists() and lane.exists()):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        board = Board.objects.get(pk=request.data['board_id'])
        lane = Lanes.objects.get(pk=request.data['column_id'])

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=board, column=lane)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def check_boardcolumn(self, board_id, column_id):
        board_exist = Board.objects.filter(id=board_id).exists()
        lane_exist = Lanes.objects.filter(id=column_id).exists()
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
        if not self.check_boardcolumn(request.data['board_id'], request.data['column_id']):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        task = self.get_object(pk)
        if isinstance(task, Response):
            return task
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if isinstance(task, Response):
            return task
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)