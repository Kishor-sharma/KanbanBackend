from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Lanes
from .serializer import LanesSerializer

# Create your views here.
class LaneAPIView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Lanes.objects.get(pk=pk)
        except Lanes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        column = self.get_object(pk)
        if isinstance(column, Response):
            return column
        serializer = LanesSerializer(column)
        return Response(serializer.data)

    def put(self, request, pk):
        column = self.get_object(pk)
        if isinstance(column, Response):
            return column
        serializer = LanesSerializer(column, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        column = self.get_object(pk)
        if isinstance(column, Response):
            return column
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)