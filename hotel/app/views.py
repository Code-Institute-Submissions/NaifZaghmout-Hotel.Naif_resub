"""
Views of the website
"""
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Hotels, Rooms, Reservation
from .exceptions import (
    RenderingHotels,
    UserNameNotAvailable,
    UserNameAlreadyExists,
    IncorrectCredentials,
)

# Create your views here.


def home(request):
    """
    Home Page of the website
    """
    all_location = (
        Hotels.objects.values_list("hotel_location", "id").distinct().order_by()
    )
    if request.method != "POST":
        data: dict = {"all_location": all_location}
        response = render(request, "index.html", data)
        return HttpResponse(response)

    try:
        hotels: list = Hotels.objects.all().get(
            id=int(float(request.POST["search_location"]))
        )
        room_reservations: list = []

        # for finding the reserved rooms on this time period for excluding from the query set
        for each_reservation in Reservation.objects.all():
            if str(each_reservation.check_in_date) < str(request.POST["cin"]) and str(
                each_reservation.check_out_date
            ) < str(request.POST["cout"]):
                pass
            elif str(each_reservation.check_in_date) > str(request.POST["cin"]) and str(
                each_reservation.check_out_date
            ) > str(request.POST["cout"]):
                pass
            else:
                room_reservations.append(each_reservation.room.id)

        rooms: list = (
            Rooms.objects.all()
            .filter(hotel=hotels, max_capacity=int(request.POST["capacity"]))
            .exclude(id__in=room_reservations)
        )

        if len(rooms) == 0:
            messages.warning(
                request, "Sorry No Rooms Are Available on this time period"
            )
        data = {"rooms": rooms, "all_location": all_location, "flag": True}
        response = render(request, "index.html", data)
    except RenderingHotels as e_x:
        messages.error(request, e_x)
        response = render(request, "index.html", {"all_location": all_location})

    return HttpResponse(response)


    def about_us(request):
    
     """
     About us page
     """
    return HttpResponse(render(request, "about.html"))




    def contact(request):

     """
     Contact page
     """
    return HttpResponse(render(request, "contact.html"))