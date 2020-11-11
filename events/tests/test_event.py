import unittest
from datetime import datetime

from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from events.models import Event


def create_event(title, description, category):
    """Create an event with the given `title`, `description` and `category`."""
    created_at = timezone.now()
    image_url = 'https://bit.ly/3jlbxGT'
    appointment_date = datetime.strptime('2020-10-29', '%Y-%m-%d').date()

    event1 = Event.objects.create(title=title, description=description, category=category, created_at=created_at,
                                  appointment_date=appointment_date, image_url=image_url)

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
        event = create_event("Walking", "Walk in Jungle", "Sport", )
        response = self.client.get(reverse('events:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, event.title)

    def test_event_category(self):
        """The event is show in according to category, when you choose category."""
        event1 = create_event("Walking", "Walk in Jungle", "Sport")
        event2 = create_event("Dinner", "Eat KFC", "Eating")
        url = reverse('events:events_by_category', args=(event1.category,))
        response = self.client.get(url)
        self.assertContains(response, event1.title)  # check that event1 is include in Sport
        self.assertNotContains(response, event2.title)  # check that event2 is not include in Sport

    def test_event_detail(self):
        """If the event is clicked, it will go to event detail page."""
        event1 = create_event("Walking", "Walk in Jungle", "Sport")
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertURLEqual('/events/Sport/walking/', url)
        self.assertContains(response, event1.description)

    @unittest.skip("Unfinished")
    def test_edit_event(self):
        """If event is edited, it will redirected to the feed page."""
        event1 = create_event("Walking", "Walk in Jungle", "Sport", )
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)

        # retrieve form
        form = response.context['event_form']

        # make some edit
        data = form.initial
        data['title'] = 'Hiking'

        # POST to the form
        response = self.client.post(url, data)

        # retrieve again
        response = self.client.get(url)
        self.assertContains(response, 'Hiking')
        self.assertRedirects(response, '/events/feed')

    def test_delete_event(self):
        """If the event is deleted, it will redirect to event detail page."""
        event1 = create_event("Walking", "Walk in Jungle", "Sport")
        url = reverse('events:delete_event', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        response = self.client.get(reverse('events:feed'))
        self.assertNotContains(response, event1.title)  # check that event1 is not on the feed.

    @unittest.skip("No convenience way to test")
    def test_invalid_event(self):
        """If the users try to invoke invalid event, it will show 404 error."""
        event1 = Event.objects.get(title='Football')
        event1.save()
        url = reverse('events:event_detail', args=(event1.category, event1.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)