from django.urls import path
from . import views

urlpatterns = [
    path('register/' , views.Sign_up),
    path('login/' , views.User_Info),
]


"""
    main apis for USERS

    ==> api/users/register/     (register)
    ==> api/users/login/        (login)
    ==> api/users/token/        (token)
"""