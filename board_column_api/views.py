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

        board_id = request.data['board_id'] 
        column_id = request.data['column_id']

        board_exist = Board.objects.filter(id=board_id).exists()
        column_exist = Lanes.objects.filter(id=column_id).exists()

        if not (board_exist and column_exist):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
class BoardColumnDetailView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, table_id):
        data_exist = BoardColumn.objects.filter(board_id=table_id).exists()
        if not data_exist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        boardcolumn = BoardColumn.objects.all().filter(board_id=table_id)
        serializer = BoardColumnSerializer(boardcolumn, many=True)
        return Response(serializer.data)