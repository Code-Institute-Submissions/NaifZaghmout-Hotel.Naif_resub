from django.urls import path
from app import views
urlpatterns = [
    path("", views.home, name="HomePage"),
    path("about", views.about_us, name="aboutpage"),
    path("contact", views.contact, name="contact")
]