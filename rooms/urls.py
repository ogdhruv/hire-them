from django import views
from django.urls import path
from .views import dashboard, rooms

urlpatterns = [
    path("", view=dashboard, name="dashboard"),
    path("rooms/", view=rooms, name="rooms"),
]
