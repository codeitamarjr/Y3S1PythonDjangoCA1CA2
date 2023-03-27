from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question, Choice

class QuestionModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text='Test question',
            pub_date=timezone.now()
        )
        self.choice1 = Choice.objects.create(
            question=self.question,
            choice_text='Choice 1',
            votes=2
        )
        self.choice2 = Choice.objects.create(
            question=self.question,
            choice_text='Choice 2',
            votes=1
        )

    def test_question_str(self):
        self.assertEqual(str(self.question), 'Test question')

    def test_question_was_published_recently(self):
        self.assertTrue(self.question.was_published_recently())

    def test_question_total_votes(self):
        self.assertEqual(self.question.total_votes(), 3)

    def test_choice_str(self):
        self.assertEqual(str(self.choice1), 'Choice 1')
