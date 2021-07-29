from django.db import models
from django.shortcuts import reverse


class News(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})