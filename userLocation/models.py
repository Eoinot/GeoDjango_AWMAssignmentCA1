from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as models_gis
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    Golf_Course_Name = models.TextField(blank=True, null=True)
    location = models_gis.PointField(null=True)

    def __str__(self):
        return f"{str(self.Longitude)},{str(self.Latitude)}"


class GolfCourse(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    golfCourseName = models.TextField(blank=True, null=True)
    location = models_gis.PointField(null=True)

    def __str__(self):
        return f"{self.golfCourseName} ({self.longitude},{self.latitude})"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
