from django.urls import path
from .views import rooms,room

urlpatterns = [
    path("", view=rooms, name="rooms"),
    path("?=<int:pk>/",view=room,name="room"),
]
