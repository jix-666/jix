# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .test_event import create_event


class JoinEventTests(TestCase):
    """Tests for Joining event."""

    def test_single_user_joins_event(self):
        """If the user joins the event. Username will be shown on attendees."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        user28 = User.objects.create_user(username='testuser28', password='secret123456')
        self.client.post(reverse('login'), {'username': 'testuser',
                                            'password': 'secret123456'}, follow=True)
        event1 = create_event("Walking", "Walk in Jungle", "Sport", user)
        self.client.get(reverse('logout'))
        self.client.post(reverse('login'), {'username': 'testuser28',
                                            'password': 'secret123456'}, follow=True)
        url = reverse('events:joining_event', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertContains(response, f'{user28.username}')

    def test_2_or_more_users_join_event(self):
        """If there are two or more users join the event. Their name will be shown on attendees."""
        # create users and event
        user1 = User.objects.create_user(username='testuser', password='secret123456')
        user2 = User.objects.create_user(username='testuser2', password='secret1234567')
        user28 = User.objects.create_user(username='testuser28', password='secret1234567')
        # user 1 login
        self.client.post(reverse('login'), {'username': 'testuser',
                                            'password': 'secret123456'}, follow=True)
        event1 = create_event("Swim", "Swim in the sea", "Sport", user2)
        # user 1 logout
        self.client.get(reverse('logout'))
        # user 2 login
        self.client.post(reverse('login'), {'username': 'testuser2',
                                            'password': 'secret1234567'}, follow=True)
        url = reverse('events:joining_event', args=(event1.category, event1.slug))
        self.client.get(url)
        # user 2 logout
        self.client.get(reverse('logout'))

        # user 28 login
        self.client.post(reverse('login'), {'username': 'testuser28',
                                            'password': 'secret1234567'}, follow=True)
        url = reverse('events:joining_event', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertContains(response, f'{user1.username}')
        self.assertContains(response, f'{user28.username}')

    def test_unauthenticated_user_join_event(self):
        """If the users is not authenticated and try to invoke joining, they will be redirect to login page."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        event1 = create_event("Walking", "Walk in Jungle", "Sport", user)
        url = reverse('events:joining_event', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/events/Sport/walking/join/', 302, 301)
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertNotContains(response, 'You')
