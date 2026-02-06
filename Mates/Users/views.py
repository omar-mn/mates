from django.shortcuts import render
from .serializers import Sign_UpSerializer , UserInfo
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from .models import account

@api_view(['POST'])
@permission_classes([AllowAny])
def Sign_up(request):
    serializer = Sign_UpSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"account created ya 7ob , enjoy!"})
        # if not account.objects.filter(email = serializer.data['email']).exists:
        #     serializer.save()
        #     return Response({"account created ya 7ob , enjoy!"})
        # else:
        #     return Response({"error" : "الاكونت دا موجود يسطا , دورلك ع ايميل تاني او اعمل login"})
    else:
        return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def User_Info(request):
    serializer = UserInfo(request.user)
    return Response({"userData" : serializer.data})
