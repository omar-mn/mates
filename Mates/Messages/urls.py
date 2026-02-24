from django.urls import path 
from . import views

urlpatterns = [
    path('send/<int:pk>/' , views.CreateMessage),
    path('mod/<int:pkR>/<int:pkM>/' , views.ModMessage),
]
