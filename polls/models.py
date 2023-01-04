from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.TextField(max_length=200)
    date_pub = models.DateTimeField('date published',auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_now(self):
        return self.date_pub >= timezone.now - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
