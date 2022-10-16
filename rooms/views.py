from django.shortcuts import render
from rooms.models import Room

def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,"rooms/rooms.html",context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,"rooms/room.html",context)
