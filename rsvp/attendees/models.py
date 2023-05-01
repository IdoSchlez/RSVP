from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, blank=True)
