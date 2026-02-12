from django.urls import path
from . import views

urlpatterns = [
    path('register/' , views.Sign_up),
    path('info/' , views.User_Info)
]


"""
    main apis for USERS

    ==> api/users/register/     (register)
    ==> api/users/token/        (token)
    ==> api/users/info/         (profile)
"""