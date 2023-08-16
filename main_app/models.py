from django.db import models
from django.urls import reverse

VARIETIES = (
    ('R', 'Roundwound'),
    ('H', 'Halfround'),
    ('F', 'Flatwound'),
    ('T', 'Tapewound'),
)

class Bass(models.Model):
    make = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    scale = models.IntegerField()
    color = models.CharField(max_length=20)
    construction = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('bass_details', kwargs={'bass_id': self.id})

class Strings(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    variety = models.CharField(
        # Name of the field in UI 
        'Type',
        max_length=1,
        choices = VARIETIES,
        default = VARIETIES[0][0]
    )
    bass = models.ForeignKey(
        Bass,
        # Deletes Strings associated with Bass
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.make} {self.model} {self.get_variety_display()}'