from django.db import models
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def save(self, *args, **kwargs):
        translator = Translator()

        try:
            if not self.question_hi and self.question:
                translated_hi = translator.translate(self.question, src="en", dest="hi")
                self.question_hi = translated_hi.text  # ✅ FIXED: No async issue

            if not self.question_bn and self.question:
                translated_bn = translator.translate(self.question, src="en", dest="bn")
                self.question_bn = translated_bn.text  # ✅ FIXED: No async issue

        except Exception as e:
            print(f"Translation error: {e}")  # Logs error but allows saving

        super().save(*args, **kwargs)
