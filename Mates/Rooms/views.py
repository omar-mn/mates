from django.shortcuts import render
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializers import CreateRoomSerializer
from rest_framework.response import Response
from .models import MemberShip , Room
from rest_framework.pagination import PageNumberPagination

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateRoom(request):
    serializer = CreateRoomSerializer(data = request.data , context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response({"room created , have fun!"})
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AvailbleRooms(request):
    rooms = Room.objects.all()
    serializer = CreateRoomSerializer(rooms , many=True , context={"request": request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AvailbleRooms(request):
    rooms = Room.objects.all()
    pagintaor = PageNumberPagination()
    pagintaor.page_size = 10
    queryset = pagintaor.paginate_queryset(rooms,request)
    serializer = CreateRoomSerializer(queryset , many=True , context={"request": request})

    return Response(serializer.data)