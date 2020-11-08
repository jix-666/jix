from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignOutTest(TestCase):
    """Tests for signing out."""

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'testuser',
            'password': 'secret123456',
            'email': 'testerman@gmail.com',
            'first_name': 'Testerman'}
        User.objects.create_user(**self.credentials)

    def test_sign_out(self):
        """If the user sign out, it will redirect to login page."""
        response = self.client.post(reverse('login'), {'username': 'testuser',
                                    'password': 'secret123456'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')

    def test_sign_out_button_is_shown(self):
        """If the user is signed in, the sign out button is shown."""
        response = self.client.post(reverse('login'), {'username': 'testuser',
                                    'password': 'secret123456'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertContains(response, 'Sign out')

    def test_sign_in_button_is_shown(self):
        """If the user is signed out, the sign in and sign up button is shown on feed page."""
        response = self.client.post(reverse('login'), {'username': 'testuser',
                                    'password': 'secret123456'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.get(reverse('logout'))
        response = self.client.get(reverse('events:feed'))
        self.assertContains(response, 'Sign in')
        self.assertContains(response, 'Sign up')
