from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from report.tests.test_report import report_and_create_event


class EventReportsTest(TestCase):
    """Test for Report Views."""

    def setUp(self):
        """Create a super user to view report feed."""
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        self.client.force_login(user=self.user)

    def test_new_report(self):
        """If event is reported, it will be show on the feed."""
        report = report_and_create_event("spam", "Hi", )
        response = self.client.get(reverse('report:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, report.event)
