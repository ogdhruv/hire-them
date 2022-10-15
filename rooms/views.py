from tempfile import TemporaryDirectory
from unittest import TestProgram
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, template_name="rooms/dashboard.html")


def rooms(request):
    return render(request, template_name="rooms/rooms.html")
