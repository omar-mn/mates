from django.shortcuts import render
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializers import CreateRoomSerializer , Join_MS ,ViewRooms
from rest_framework.response import Response
from .models import MemberShip , Room 
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone


# CREATE ROOM

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateRoom(request):
    serializer = CreateRoomSerializer(data = request.data , context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response({"room created , have fun!"})
    return Response(serializer.errors)


# MDEIFY ROOM

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def EditRoom(request,pk):
    
    try:
        room = Room.objects.get(pk = pk)
    except Room.DoesNotExist:
        return Response({"error" : "this room DoesNotExist ya broo"})
    
    if request.method == 'PUT':
        serializer = CreateRoomSerializer(room , data = request.data , partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        serializer = CreateRoomSerializer(room)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        room.delete()
        return Response({"room deleted"})


# JOIN ROOM

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JoinRoom(request,pk):
    
    try:
            room = Room.objects.get(pk = pk)
    except Room.DoesNotExist:
        return Response({"error" : "sorry the room u r trying to join DoesNotExist"})

    try:
        Mes = MemberShip.objects.filter(user = request.user  , room = room).first()
        if Mes.leftDate == None:
            Mes.leftDate = timezone.now()
            Mes.save()
            return Response({"action" : "youe left this room"})
        else:
            Mes.leftDate = None
            Mes.save()
            return Response({"joined":"you are now a member of this room , have fun!"})

    except:
        serializer = Join_MS( data = request.data , context={"request": request,"room" : room} )
        if serializer.is_valid():
            serializer.save()
            return Response({"joined":"you are now a member of this room , have fun!"})
        else :
            return Response(serializer.errors)

# ALL ROOMS

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AvailbleRooms(request):
    rooms = Room.objects.all()
    pagintaor = PageNumberPagination()
    pagintaor.page_size = 10
    queryset = pagintaor.paginate_queryset(rooms,request)
    serializer = ViewRooms(queryset , many=True , context={"request": request})

    return Response(serializer.data)

