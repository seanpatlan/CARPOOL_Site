from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Ride(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    car = models.PositiveSmallIntegerField()
    num_patrons = models.PositiveSmallIntegerField()
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    comments = models.TextField()
    time = models.DateTimeField(default=timezone.now())  # Alternative: default=timezone.now
    waiting = models.BooleanField()
    riding = models.BooleanField()
    done = models.BooleanField()
    cancelled = models.BooleanField()
    deleted = models.BooleanField()
    # posted_by = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

