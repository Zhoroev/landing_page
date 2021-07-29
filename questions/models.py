from django.db import models


class Question(models.Model):
    contact = models.CharField(max_length=80)
    question = models.TextField()
