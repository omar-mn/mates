from django.urls import path 
from . import views


urlpatterns = [
    path('create/' , views.CreateRoom),
    path('' , views.AvailbleRooms),
    path('modify/<int:pk>/', views.EditRoom),
    path('membership/<int:pk>/' , views.JoinRoom)
]

"""
    main apis for ROOMS

    ==> api/rooms/ '' /         (all rooms)
    ==> api/rooms/create/       (add room)
    ==> api/rooms/modify/       (modify room)
    ==> api/rooms/membership/   (joinnnnnn)
"""