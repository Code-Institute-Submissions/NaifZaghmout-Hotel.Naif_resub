from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class CustomAuthViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_user_sign_up_view(self):
        response = self.client.post(
            reverse("usersignup"),
            {
                "username": "newuser",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the user was created and logged in
        new_user = User.objects.get(username="newuser")
        self.assertTrue(new_user.is_authenticated)

    def test_staff_sign_up_view(self):
        response = self.client.post(
            reverse("staffsignup"),
            {
                "username": "newstaff",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the staff user was created and logged in
        new_staff = User.objects.get(username="newstaff")
        self.assertTrue(new_staff.is_authenticated)
        self.assertTrue(new_staff.is_staff)

    def test_user_log_sign_page_view(self):
        response = self.client.post(
            reverse("userloginpage"),
            {
                "email": self.test_user.username,
                "pswd": "testpassword",
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the user is logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logoutuser_view(self):
        response = self.client.get(reverse("logout"))

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the user is logged out
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_staff_log_sign_page_view(self):
        response = self.client.post(
            reverse("staffloginpage"),
            {
                "username": "testuser",
                "password": "testpassword",
            },
        )

        self.assertEqual(
            response.status_code, 302
        )  # Check if the redirect is successful

        # Check if the staff user is logged in
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertFalse(response.wsgi_request.user.is_staff)
