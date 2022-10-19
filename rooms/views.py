from django.shortcuts import render, redirect
from rooms.forms import RoomForm
from rooms.models import Room


def rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "rooms/rooms.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "rooms/room.html", context)


def createRoom(request):
    form = RoomForm()
    # process data from form
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            # the below line will save the form data in model Room
            form.save()
            return redirect("rooms")
    context = {"form": form}
    return render(request, "rooms/room_form.html", context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("rooms")
    context = {"form": form}
    return render(request, "rooms/room_form.html", context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("rooms")
    return render(request,"rooms/delete_room.html",{"obj":room})
    