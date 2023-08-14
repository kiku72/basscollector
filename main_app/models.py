from django.db import models
from django.urls import reverse

# Create your models here.
class Bass(models.Model):
    make = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    scale = models.IntegerField()
    color = models.CharField(max_length=20)
    construction = models.CharField(max_length=50)
    # Changing this instance method
    # does not impact the database, therefore
    # no makemigrations is necessary
    def __str__(self):
        return f'{self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('bass_details', kwargs={'bass_id': self.id})