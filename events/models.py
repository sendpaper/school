from django.db import models

# Create your models here.

class LostItem(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    catagory = models.CharField(max_length=100)
    details = models.TextField()

class FoundItem(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    catagory = models.CharField(max_length=100)
    details = models.TextField()