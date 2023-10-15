from django.test import TestCase

# Create your tests here.


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "testuser"
        self.password = "testpassword"

    def test_user_sign_up(self):
        response = self.client.post(
            reverse("usersignup"),
            {
                "username": self.username,
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertEqual(response.status_code, 302)  # expecting a redirect
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_staff_sign_up(self):
        response = self.client.post(
            reverse("staffsignup"),
            {
                "username": self.username,
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            User.objects.filter(username=self.username, is_staff=True).exists()
        )

    def test_user_login(self):
        User.objects.create_user(username=self.username, password=self.password)
        response = self.client.post(
            reverse("userloginpage"), {"email": self.username, "pswd": self.password}
        )
        self.assertEqual(response.status_code, 302)  # assuming it redirects to home
        self.assertIn(
            "_auth_user_id", self.client.session
        )  # check if user is logged in


        
        