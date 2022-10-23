from django.urls import path
from .views import createRoom, rooms, room, updateRoom, deleteRoom

urlpatterns = [
    path("", view=rooms, name="rooms"),
    path("?=<int:pk>/", view=room, name="room"),
    path("create-room/", view=createRoom, name="create_room"),
    path("?=<int:pk>/update-room/", view=updateRoom, name="update_room"),
    path("?=<int:pk>/delete-room/", view=deleteRoom, name="delete_room"),
]
