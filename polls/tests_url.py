from django.test import TestCase
from django.urls import reverse
from django.utils import timezone


from .models import Question

class PollsViewsTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text='Test question',
            pub_date=timezone.now()
        )

    def test_index_view(self):
        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.question_text)
