from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from Rooms.models import Room
from .serializers import MessageSerializer , ModMessageSerializer
from Rooms.models import MemberShip
from .models import Message

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateMessage(request , pk):

    try:
        room = Room.objects.get(pk = pk)
    except:
        return Response({"error" : "this room doesnt exist"})
    
    Mes = MemberShip.objects.filter(user = request.user , room = room).first()
    if Mes:
        if Mes.leftDate is None:
            serializer = MessageSerializer( data = request.data , context = {"request": request , "Room":room })
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({"you are not a member of thid room!"})
    else:
        return Response({"you are not a member of thid room!"})
    

@api_view(['PUT' , 'DELETE'])
@permission_classes([IsAuthenticated])
def ModMessage(request , pkR , pkM):

    try:
        message = Message.objects.get(pk = pkM)
        room = Room.objects.get(pk = pkR)
    except:
        return Response({"eorro" : "this message doesnt exist"})
    
    if request.method == 'PUT':
        if request.user == message.user:
            serializer = ModMessageSerializer(message , data = request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message edited"})
            else:
                return Response(serializer.errors)
        else:
            return Response({"you can't edite this message!"})
        
    if request.method == 'DELETE':
        Mes = MemberShip.objects.filter(user = request.user , room = room).first()
        if request.user == message.user or Mes.role == 'owner':
            message.delete()
            return Response({"message deleted"})
        else:
            return Response({"you can't delet this message!"})