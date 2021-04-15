from django.db import models
from django.urls import reverse

class Word(models.Model):
    word = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True) #, upload_to='images/'
    translation = models.TextField()

    # def get_absolute_url(self):
    #     return reverse('word-detail', kwargs={'id':self.id})#f"/products/{self.id}/"
