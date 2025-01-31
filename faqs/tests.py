from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python framework.")

    def test_translation(self):
        self.assertIsNotNone(self.faq.question_hi)  # Ensure Hindi translation exists
        self.assertIsNotNone(self.faq.question_bn)  # Ensure Bengali translation exists

