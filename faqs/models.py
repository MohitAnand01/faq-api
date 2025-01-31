import asyncio
from googletrans import Translator
from django.db import models
from ckeditor.fields import RichTextField

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def save(self, *args, **kwargs):
        """ Use asyncio.run() to handle async translation calls """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        if not self.question_hi:
            self.question_hi = loop.run_until_complete(translator.translate(self.question, src='en', dest='hi')).text

        if not self.question_bn:
            self.question_bn = loop.run_until_complete(translator.translate(self.question, src='en', dest='bn')).text

        super().save(*args, **kwargs)
