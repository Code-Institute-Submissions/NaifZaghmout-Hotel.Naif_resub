from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Hotels, Rooms


class StaffViewTestCase(TestCase):
    # ...[setUp and tearDown methods]...

    def test_add_new_location_with_staff_user(self):
        self.client.login(username="staffuser", password="testpassword")
        response = self.client.post(
            reverse("addnewlocation"),
            {
                "new_owner": "owner2",
                "new_city": "city2",
                "new_state": "state2",
                "new_country": "country2",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Hotels.objects.filter(hotel_location="city2").exists())



    def test_all_bookings_with_staff_user(self):
        self.client.login(username="staffuser", password="testpassword")
        response = self.client.get(reverse("allbookigs"))
        self.assertEqual(response.status_code, 200)