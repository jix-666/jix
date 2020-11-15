from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from report.tests.test_report import report_and_create_event


class ReportsDeleteTest(TestCase):
    """Test for Report Views."""

    def setUp(self):
        """Create a super user to view report feed."""
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')

    def test_superuser_delete_report(self):
        """If the user is superuser, he or she can delete report."""
        self.client.force_login(user=self.user)
        report = report_and_create_event("hate-speech", "Hi", )
        url = reverse('report:delete_report', args=(report.report_type, report.id))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('report:feed'))
        self.assertContains(response, "No reports.")

    def test_non_superuser_delete_report(self):
        """If the user is not superuser, he or she can't delete report.

        The message permission denied will be shown.

        """
        # login with non super user account
        User.objects.create_user(username='testuser2', password='secret123456')
        self.client.post(reverse('login'), {'username': 'testuser2',
                                            'password': 'secret123456'}, follow=True)

        report = report_and_create_event("hate-speech", "Hi", )
        url = reverse('report:delete_report', args=(report.report_type, report.id))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/events/')

        # get message from context and check that expected text is there
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Permission denied." in message.message)

    def test_non_authenticated_user_delete_report(self):
        """If non authenticated user try to delete report, he or she will be redirect to event feed."""
        report = report_and_create_event("hate-speech", "Hi", )
        url = reverse('report:delete_report', args=(report.report_type, report.id))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
