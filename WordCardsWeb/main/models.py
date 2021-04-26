from django.db import models
from django.urls import reverse

class Word(models.Model):
    word = models.CharField(max_length=200)
    image = models.ImageField(
    upload_to='../images/', default='../images/default.jpg', blank=True
    )
    translation = models.CharField(max_length=500)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('word-detail', kwargs={'pk':self.pk})#f"/products/{self.id}/"

    def delete_img(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def delete_def(self, *args, **kwargs):

        super().delete(*args, **kwargs)
