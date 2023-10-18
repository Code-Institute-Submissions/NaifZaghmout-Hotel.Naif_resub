from django.shortcuts import render

# Create your views here.

import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Hotels, Rooms, Reservation
from app.exceptions import (
    RenderingHotels,
    UserNameNotAvailable,
    UserNameAlreadyExists,
    IncorrectCredentials,
)
# Create your views here.
@login_required(login_url="/staff")
def add_new_location(request):
    """
    Add new location to the list
    """
    if request.method == "POST" and request.user.is_staff:
        owner = request.POST["new_owner"]
        location = request.POST["new_city"]
        state = request.POST["new_state"]
        country = request.POST["new_country"]

        hotels = Hotels.objects.all().filter(hotel_location=location, hotel_state=state)
        if hotels:
            messages.warning(request, "Sorry City at this Location already exist")
            return redirect("staffpanel")

        new_hotel = Hotels()
        new_hotel.hotel_owner = owner
        new_hotel.hotel_location = location
        new_hotel.hotel_state = state
        new_hotel.hotel_country = country
        new_hotel.save()
        messages.success(request, "New Location Has been Added Successfully")
        return redirect("staffpanel")

    return HttpResponse("Not Allowed")



@login_required(login_url="/staff")
def all_bookings(request):
    """
    Show all bookings
    Staff login required
    """
    bookings = Reservation.objects.all()
    if not bookings:
        messages.warning(request, "No Bookings Found")
    return HttpResponse(
        render(request, "staff/all_bookings.html", {"bookings": bookings})
    )




@login_required(login_url="/staff")
def view_room(request):
    """
    View Room
    """
    room_id = request.GET["roomid"]
    room = Rooms.objects.all().get(id=room_id)

    reservation = Reservation.objects.all().filter(room=room)
    return HttpResponse(
        render(
            request, "staff/view_room.html", {"room": room, "reservations": reservation}
        )
    )




@login_required(login_url="/staff")
def panel(request):
    """
    Staff Panel Page
    """
    if request.user.is_staff == False:
        return HttpResponse("Access Denied")
        

    rooms = Rooms.objects.all()
    total_rooms: int = len(rooms) if len(rooms) > 0 else 1
    available_rooms: int = len(Rooms.objects.all().filter(availability_status="1"))
    unavailable_rooms: int = len(Rooms.objects.all().filter(availability_status="2"))
    reserved: int = len(Reservation.objects.all())