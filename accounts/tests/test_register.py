from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse


class RegistrationTest(TestCase):
    """Tests for registration."""

    def test_register_page(self):
        """If registration page is available, it will shoe the register template and status Code 200 OK."""
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertEqual(response.status_code, 200)

    def test_successful_registration(self):
        """If the registration progress is completed, it will redirect to login page."""
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser1@gmail.com', 'first_name': 'Testerman',
            'password1': 'secret123456', 'password2': 'secret123456'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')

    def test_register_with_exists_username(self):
        """If the username is already taken, the error message will be shown."""
        User.objects.create(username='testuser', email='testerman@gmail.com', password='secret')
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser2@gmail.com', 'first_name': 'Testerman2',
            'password1': 'secret123456', 'password2': 'secret123456'})
        self.assertContains(response, 'A user with that username already exists.')

    def test_register_with_invalid_email(self):
        """If an email doesn't have @, it not an email, it will not redirect after submit."""
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser2gmail.com', 'first_name': 'Testerman2',
            'password1': 'secret123456', 'password2': 'secret123456'})
        self.assertEqual(response.status_code, 200)

    def test_register_with_non_matching_password(self):
        """If the password1 and password2 didn't match, the error message will be shown."""
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser2@gmail.com', 'first_name': 'Testerman2',
            'password1': 'secret123456', 'password2': 'secret'})
        self.assertContains(response, 'The two password fields didn’t match.')

    def test_register_with_only_numeric_password(self):
        """If the password contains only numeric, the error message will be shown."""
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser2@gmail.com', 'first_name': 'Testerman2', 'password1': '123456',
            'password2': '123456'})
        self.assertContains(response, 'This password is entirely numeric.')

    def test_register_with_short_password(self):
        """If the password is shorter than 8 characters, the error message will be shown."""
        """If the password contains only numeric, the error message will be shown."""
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser2@gmail.com', 'first_name': 'Testerman2', 'password1': 'sec456',
            'password2': 'sec456'})
        self.assertContains(response, 'This password is too short. It must contain at least 8 characters.')

    def test_register_with_too_common_password(self):
        """If the password is too common, the error message will be shown.

        Too common password can be found on https://xato.net/passwords/more-top-worst-passwords/.

        """
        response = self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'testuser2@gmail.com', 'first_name': 'Testerman2',
            'password1': 'aaaaaaaa', 'password2': 'aaaaaaaa'})
        self.assertContains(response, 'This password is too common.')
