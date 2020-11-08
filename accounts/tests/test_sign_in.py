from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignInTest(TestCase):
    """Tests for signing in."""

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'testuser',
            'password': 'secret123456',
            'email': 'testerman@gmail.com',
            'first_name': 'Testerman'}
        User.objects.create_user(**self.credentials)

    def test_sign_in(self):
        """If the login is successful, user will be redirect to event feed page and greet user."""
        response = self.client.post(reverse('login'), {'username': 'testuser',
                                    'password': 'secret123456'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, '/events/')
        self.assertContains(response, f"Hello, {response.context['user'].first_name}")

    def test_sign_in_with_wrong_password(self):
        """User cannot sign in if the password is incorrect, an error message will be shown."""
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '1234'}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertContains(response, 'Username or Password is incorrect.')

    def test_sign_in_with_wrong_username(self):
        """User cannot sign in if the username is incorrect, an error message will be shown."""
        response = self.client.post(reverse('login'), {'username': 'John', 'password': 'secret123456'}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertContains(response, 'Username or Password is incorrect.')

    def test_sign_in_without_password(self):
        """User cannot sign in if the password is not enter, an error message will be shown."""
        response = self.client.post(reverse('login'), {'username': 'testuser'}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertContains(response, 'Username or Password is incorrect.')
