from django.shortcuts import render
# from .serializers import Sign_UpSerializer , UserInfo , JoinRoom
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from .models import account





####################################################################3


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def Sign_up(request):
#     serializer = Sign_UpSerializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({"account created ya 7ob , enjoy!"})
#     else:
#         return Response(serializer.errors)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def User_Info(request):
#     serializer = UserInfo(request.user , context={"request": request})
#     return Response({"userData" : serializer.data})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def Join(request):
#     serializer = JoinRoom(data = request.data)
    