from django.db import models
from django.shortcuts import reverse


class Blog(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=128)
    birthdate = models.DateField()
    phone = models.IntegerField()
    

    # def __str__(self):
    #     return self.title
    #
    # def get_absolute_url(self):
    #     return reverse('post_detail_url', kwargs={'id': self.id})
    #
    # def get_update_url(self):
    #     return reverse('post_update_url', kwargs={'id': self.id})
    #
    # def get_delete_url(self):
    #     return reverse('post_delete_url', kwargs={'id': self.id})
