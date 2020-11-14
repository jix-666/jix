import unittest

from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from django.contrib.auth.models import User
from .test_event import create_event


class EditEventTests(TestCase):
    """Tests for Editing event."""

    @unittest.skip('unfinished')
    def test_edit_event(self):
        """If event is edited, it will redirected to the feed page."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        self.client.post(reverse('login'), {'username': 'testuser',
                                            'password': 'secret123456'}, follow=True)
        event1 = create_event("Walking", "Walk in Jungle", "Sport", user)
        url = reverse('events:edit_event', args=(event1.category, event1.slug))
        self.client.post(url, {event1.title: 'Hiking'}, follow=True)
        response = self.client.get(reverse('events:feed'))
        self.assertContains(response, 'Hiking')
        self.assertRedirects(response, '/events/feed')
