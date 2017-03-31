from django.db import models
from location.models import Location


# Create your models here.
class Character(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthplace = models.ForeignKey(Location, related_name='birthplace')
    description = models.CharField(max_length=255)
    times_killed = models.IntegerField(default=0, )
    location_of_death = models.ForeignKey(Location, blank=True, null=True, related_name='location_of_death')
    murderer = models.ForeignKey('self', blank=True, null=True)
    manner_of_death = models.CharField(max_length=255, blank=True, null=True)
    times_won_throne = models.IntegerField(default=0)
    times_survived = models.IntegerField(default=0)
    image = models.ImageField(upload_to='/images/', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
