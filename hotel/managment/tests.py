from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from app.models import Hotels, Rooms, Reservation


class ManagmentViewsTestCase(TestCase):
    def setUp(self):
        # Create a staff user
        self.staff_user = User.objects.create_user(
            username="staffuser", password="testpassword", is_staff=True
        )
        self.client = Client()

    def test_add_new_location_view(self):
        # Log in the staff user
        self.client.login(username="staffuser", password="testpassword")

        response = self.client.post(
            reverse("addnewlocation"),
            {
                "new_owner": "New Owner",
                "new_city": "New City",
                "new_state": "New State",
                "new_country": "New Country",
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the new location was added
        new_hotel = Hotels.objects.get(
            hotel_location="New City", hotel_state="New State"
        )
        self.assertEqual(new_hotel.hotel_owner, "New Owner")

    def test_all_bookings_view(self):
        # Log in the staff user
        self.client.login(username="staffuser", password="testpassword")

        response = self.client.get(reverse("allbookigs"))

        self.assertEqual(
            response.status_code, 200
        )  # Check if the view returns a successful response

        # Add more assertions as needed based on the view's logic

    def test_view_room_view(self):
        # Create a room for testing
        test_hotel = Hotels.objects.create(
            hotel_name="Test Hotel",
            hotel_owner="Test Owner",
            hotel_location="Test City",
            hotel_state="Test State",
            hotel_country="Test Country",
        )
        test_room = Rooms.objects.create(
            room_type="1",
            max_capacity=2,
            room_price=100,
            room_size=20,
            hotel=test_hotel,
            availability_status="1",
            room_number=101,
        )

        # Log in the staff user
        self.client.login(username="staffuser", password="testpassword")

        response = self.client.get(reverse("view_room") + f"?roomid={test_room.id}")

        self.assertEqual(
            response.status_code, 200
        )  # Check if the view returns a successful response

        # Add more assertions as needed based on the view's logic

    def test_panel_view(self):
        # Log in the staff user
        self.client.login(username="staffuser", password="testpassword")

        response = self.client.get(reverse("staffpanel"))

        self.assertEqual(
            response.status_code, 200
        )  # Check if the view returns a successful response

        # Add more assertions as needed based on the view's logic

    def test_edit_room_view(self):
        # Create a room for testing
        test_hotel = Hotels.objects.create(
            hotel_name="Test Hotel",
            hotel_owner="Test Owner",
            hotel_location="Test City",
            hotel_state="Test State",
            hotel_country="Test Country",
        )
        test_room = Rooms.objects.create(
            room_type="1",
            max_capacity=2,
            room_price=100,
            room_size=20,
            hotel=test_hotel,
            availability_status="1",
            room_number=101,
        )

        # Log in the staff user
        self.client.login(username="staffuser", password="testpassword")

        response = self.client.post(
            reverse("edit_room") + f"?roomid={test_room.id}",
            {
                "roomid": test_room.id,
                "hotel": test_hotel.id,
                "roomtype": "2",
                "capacity": 3,
                "price": 120,
                "size": 25,
                "status": "2",
                "roomnumber": 102,
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the room details were updated
        updated_room = Rooms.objects.get(id=test_room.id)
        self.assertEqual(updated_room.room_type, "2")
        self.assertEqual(updated_room.max_capacity, 3)
        self.assertEqual(updated_room.room_price, 120)
        self.assertEqual(updated_room.room_size, 25)
        self.assertEqual(updated_room.availability_status, "2")
        self.assertEqual(updated_room.room_number, 102)

    def test_add_new_room_view(self):
        # Create a hotel for testing
        test_hotel = Hotels.objects.create(
            hotel_name="Test Hotel",
            hotel_owner="Test Owner",
            hotel_location="Test City",
            hotel_state="Test State",
            hotel_country="Test Country",
        )

        # Log in the staff user
        self.client.login(username="staffuser", password="testpassword")

        response = self.client.post(
            reverse("addroom"),
            {
                "hotel": test_hotel.id,
                "roomtype": "1",
                "capacity": 2,
                "price": 100,
                "size": 20,
                "status": "1",
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the new room was added
        new_room = Rooms.objects.get(hotel=test_hotel)
        self.assertEqual(new_room.room_type, "1")
        self.assertEqual(new_room.max_capacity, 2)
        self.assertEqual(new_room.room_price, 100)
        self.assertEqual(new_room.room_size, 20)
        self.assertEqual(new_room.availability_status, "1")
