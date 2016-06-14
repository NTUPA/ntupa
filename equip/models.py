from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)

class Equipment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)