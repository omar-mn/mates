from django.urls import path 
from . import views


urlpatterns = [
    path('create/' , views.CreateRoom),
    path('' , views.AvailbleRooms),
]

"""
    main apis for ROOMS

    ==> api/rooms/        (all rooms)
    ==> api/create/       (add room)
"""