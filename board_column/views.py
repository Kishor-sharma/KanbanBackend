from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import BoardColumn
from board_api.models import Board
from column_api.models import Lanes
from .serializer import BoardColumnSerializer

# Create your views here.
class BoardColumnAPIView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        alldata = BoardColumn.objects.all()
        serializer = BoardColumnSerializer(alldata, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardColumnSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN) 

        if not Board.objects.filter(id=request.data['boardID']).exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        if not Lanes.objects.filter(id=request.data['columnID']).exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class BoardColumnDetailView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, tableID):
        data_exist = BoardColumn.objects.filter(boardID=tableID).exists()
        if not data_exist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        boardcolumn = BoardColumn.objects.all().filter(boardID=tableID)
        serializer = BoardColumnSerializer(boardcolumn, many=True)
        return Response(serializer.data)