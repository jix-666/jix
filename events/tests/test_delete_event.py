from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.
from django.urls import reverse

from .test_event import create_event
from ..models import Event


class DeleteEventTests(TestCase):
    """Tests for Deleting event."""

    def test__delete_your_event(self):
        """If the users owned the poll, he or she can deleted event and it will redirect to event detail page."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        self.client.post(reverse('login'), {'username': 'testuser',
                                            'password': 'secret123456'}, follow=True)
        event1 = create_event("Walking", "Walk in Jungle", "sport", user)
        url = reverse('events:delete_event', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        response = self.client.get(reverse('events:feed'))
        self.assertNotContains(response, event1.title)  # check that event1 is not on the feed.

    def test_delete_without_login(self):
        """If the user is not authenticated and try to delete event it will redirect to login page."""
        created_at = timezone.now()
        image_upload = 'media/images/TAE_0028.jpg'
        appointment_date = datetime.strptime('2020-10-29', '%Y-%m-%d').date()
        event1 = Event.objects.create(title="Walking", description="Walk in Jungle", category="Sport",
                                      created_at=created_at,
                                      appointment_date=appointment_date, image_upload=image_upload)
        url = reverse('events:delete_event', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/events/Sport/walking/delete/', 302, 301)
        response = self.client.get(reverse('events:feed'))
        self.assertContains(response, event1.title)  # check that event1 is still on the feed.

    def test_delete_event_by_others(self):
        """If the users don't own the poll, he or she can't deleted event and message will be shown."""
        User.objects.create_user(username='testuser', password='secret123456')
        user2 = User.objects.create_user(username='testuser2', password='secret1234567')
        self.client.post(reverse('login'), {'username': 'testuser',
                                            'password': 'secret123456'}, follow=True)
        event = create_event("Swimming", "Swim in the sea", "Sport", user2)
        response = self.client.get(reverse('events:delete_event', args=(event.category, event.slug)))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        response = self.client.get(reverse('events:feed'))
        self.assertContains(response, event.title)  # check that event is still on the feed.
