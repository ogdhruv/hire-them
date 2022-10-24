from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from rooms.forms import RoomForm
from rooms.models import Room


def rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "rooms/rooms.html", context)


@login_required
def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()
    context = {"room": room, "messages": messages}
    return render(request, "rooms/room.html", context)


@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("rooms")
    return render(request, "rooms/delete_room.html", {"obj": room})
