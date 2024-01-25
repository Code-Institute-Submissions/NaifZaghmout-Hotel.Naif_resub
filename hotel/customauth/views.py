import datetime
from django.shortcuts import render, redirect, get_object_or_404
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


def create_user(request, user_type):
    """
    Generic function for user and staff sign-up
    """
    if request.method != "POST":
        return HttpResponse("Access Denied")

    user_name = request.POST["username"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]

    if password1 != password2:
        messages.warning(request, "Password didn't match")
        return redirect(f"{user_type}loginpage")

    try:
        user = User.objects.get(username=user_name)
        messages.warning(
            request, f"Username {user_type.capitalize()} Not Available")
        return redirect(f"{user_type}loginpage")
    except User.DoesNotExist:
        new_user = User.objects.create_user(
            username=user_name, password=password1)
        new_user.is_superuser = False
        new_user.is_staff = user_type == "staff"
        new_user.save()
        messages.success(request, f"{
            user_type.capitalize()} Registration Successful")
        return redirect(f"{user_type}loginpage")


def user_sign_up(request):
    """
    User Sign Up page
    """
    return create_user(request, "user")


def staff_sign_up(request):
    """
    Staff Sign Up page
    """
    return create_user(request, "staff")


def user_log_sign_page(request):
    """
    User SignUp/ Login Page
    """
    if request.method != "POST":
        return render(request, "user/user_login_signup.html")

    Username = request.POST["Username"]
    password = request.POST["pswd"]

    user = authenticate(username=Username, password=password)

    if user is not None and user.is_staff:
        messages.error(request, "Incorrect Username or Password")
        return redirect("staffloginpage")

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully logged in")
        return redirect("HomePage")

    messages.warning(request, "Incorrect Username or Password")
    return redirect("userloginpage")


def logoutuser(request):
    """
    Logout user
    """
    if request.method == "GET":
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("HomePage")
    else:
        print("Logout unsuccessful")
        return redirect("userloginpage")


def staff_log_sign_page(request):
    """
    Staff login page
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            return redirect("staffpanel")
        else:
            messages.success(request, "Incorrect Username or Password")
            return redirect("staffloginpage")

    return render(request, "staff/staff_login_signup.html")
