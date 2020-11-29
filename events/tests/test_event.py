import unittest
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from events.models import Event


def create_event(title, description, category, user):
    """Create an event with the given `title`, `description` and `category`."""
    created_at = timezone.now()
    image_upload = 'media/images/TAE_0028.jpg'
    appointment_date = datetime.strptime('2020-10-29', '%Y-%m-%d').date()

    event1 = Event.objects.create(title=title, description=description, category=category, created_at=created_at,
                                  appointment_date=appointment_date, image_upload=image_upload, user=user)

    event1.save()
    return event1


class EventViewsTests(TestCase):
    """Test for Event Views."""

    def test_no_events(self):
        """If no events exist, an appropriate message is displayed."""
        response = self.client.get(reverse('events:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events.")
        self.assertQuerysetEqual(response.context['all_events'], [])

    def test_new_event(self):
        """If event is created, it will be show on the feed page."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        event = create_event("Walking", "Walk in Jungle", "sport", user)
        response = self.client.get(reverse('events:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, event.title)

    def test_event_category(self):
        """The event is show in according to category, when you choose category."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        event1 = create_event("Walking", "Walk in Jungle", "sport", user)
        event2 = create_event("Dinner", "Eat KFC", "eating", user)
        url = reverse('events:events_by_category', args=(event1.category,))
        response = self.client.get(url)
        self.assertContains(response, event1.title)  # check that event1 is include in Sport
        self.assertNotContains(response, event2.title)  # check that event2 is not include in Sport

    def test_event_detail(self):
        """If the event is clicked, it will go to event detail page."""
        user = User.objects.create_user(username='testuser', password='secret123456')
        event1 = create_event("Walking", "Walk in Jungle", "sport", user)
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertURLEqual('/events/sport/walking/', url)
        self.assertContains(response, event1.description)

    def test_invalid_event(self):
        """If the users try to invoke invalid event, it will redirect to event feed and shown Not Found."""
        url = reverse('events:event_detail', args=('sport', 'Football'))
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, '/events/')
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'Event not found.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
