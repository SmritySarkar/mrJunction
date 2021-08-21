from django.db import models

# Create your models here.


class Book(models.Model):
    begin = models.CharField(max_length=20)
    destination = models.CharField(max_length=30)
    depart = models.DateTimeField()
    back = models.DateTimeField()
    adult = models.CharField(max_length=20)
    children = models.CharField(max_length=20)
    travelClass = models.CharField(max_length=20)
