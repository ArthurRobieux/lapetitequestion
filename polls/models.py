import datetime

from django.db import models
from django.utils import timezone


class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def was_published_today(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name="questions", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.description
