from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication, status
from django.contrib.auth.models import User
from .models import BoardColumn
from board_api.models import Board
from column_api.models import Lanes
from .serializer import BoardColumnSerializer

# Create your views here.
class BoardColumnAPIView(APIView):
    def get(self, request):
        alldata = BoardColumn.objects.all()
        serializer = BoardColumnSerializer(alldata, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardColumnSerializer(data=request.data)

        if not Board.objects.filter(id=request.data["boardID"]).exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        if not Lanes.objects.filter(id=request.data["columnID"]).exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

class BoardColumnDetailView(APIView):
    def get_object(self, pk):
        try:
            return BoardColumn.objects.get(pk=pk)
        except BoardColumn.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_tableColumn(self, tableID):
        try:
            return BoardColumn.objects.filter(boardID=tableID)
        except BoardColumn.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, tableID):
        boardcolumn = self.get_tableColumn(tableID)
        serializer = BoardColumnSerializer(boardcolumn, many=True)
        return Response(serializer.data)