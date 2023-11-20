from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from app.models import Hotels, Rooms, Reservation
from app.exceptions import (
    RenderingHotels,
    UserNameNotAvailable,
    UserNameAlreadyExists,
    IncorrectCredentials,
)


@login_required(login_url="/staff")
@user_passes_test(lambda user: user.is_staff, login_url='/access-denied/')
def add_new_location(request):
    """
    Add a new location to the list
    """
    if request.method == "POST" and request.user.is_staff:
        owner = request.POST["new_owner"]
        location = request.POST["new_city"]
        state = request.POST["new_state"]
        country = request.POST["new_country"]

        hotels = Hotels.objects.filter(hotel_location=location, hotel_state=state)
        if hotels.exists():
            messages.warning(request, "Sorry, a City at this Location already exists")
            return redirect("staffpanel")

        new_hotel = Hotels(
            hotel_owner=owner,
            hotel_location=location,
            hotel_state=state,
            hotel_country=country
        )
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
    room = get_object_or_404(Rooms, id=room_id)

    reservation = Reservation.objects.filter(room=room)
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
    if not request.user.is_staff:
        return HttpResponse("Access Denied")

    rooms = Rooms.objects.all()
    total_rooms = rooms.count()
    available_rooms = len(Rooms.objects.filter(availability_status="1"))
    unavailable_rooms = len(Rooms.objects.filter(availability_status="2"))
    reserved = len(Reservation.objects.all())

    hotel = Hotels.objects.values_list("hotel_location", "id").distinct().order_by()

    response = render(
        request,
        "staff/staff_panel.html",
        {
            "location": hotel,
            "reserved": reserved,
            "rooms": rooms,
            "total_rooms": total_rooms,
            "available": available_rooms,
            "unavailable": unavailable_rooms,
        },
    )
    return HttpResponse(response)


@login_required(login_url="/staff")
def edit_room(request):
    """
    Update the room information
    """
    if not request.user.is_staff:
        return HttpResponse("Access Denied")

    if request.method == "POST" and request.user.is_staff:
        old_room = get_object_or_404(Rooms, id=int(request.POST["roomid"]))
        hotel = get_object_or_404(Hotels, id=int(request.POST["hotel"]))

        old_room.room_type = request.POST["roomtype"]
        old_room.max_capacity = int(request.POST["capacity"])
        old_room.room_price = int(request.POST["price"])
        old_room.room_size = int(request.POST["size"])
        old_room.hotel = hotel
        old_room.availability_status = request.POST["status"]
        old_room.room_number = int(request.POST["roomnumber"])

        old_room.save()
        messages.success(request, "Room Details Updated Successfully")
        return redirect("staffpanel")

    room_id = request.GET["roomid"]
    room = get_object_or_404(Rooms, id=room_id)
    response = render(request, "staff/edit_room.html", {"room": room})
    return HttpResponse(response)


@login_required(login_url="/staff")
def add_new_room(request):
    """
    Add a new room to the list
    """
    if not request.user.is_staff:
        return HttpResponse("Access Denied")

    if request.method == "POST":
        total_rooms = Rooms.objects.count()
        new_room = Rooms()
        hotel = get_object_or_404(Hotels, id=int(request.POST["hotel"]))

        new_room.room_number = total_rooms + 1
        new_room.room_type = request.POST["roomtype"]
        new_room.max_capacity = int(request.POST["capacity"])
        new_room.room_size = int(request.POST["size"])
        new_room.hotel = hotel
        new_room.availability_status = request.POST["status"]
        new_room.room_price = request.POST["price"]

        new_room.save()
        messages.success(request, "New Room Added Successfully")

    return redirect("staffpanel")
