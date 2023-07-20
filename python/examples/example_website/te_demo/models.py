from django.db import models


# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=100, null=True)
    objects = models.Manager


class Category(models.Model):
    category = models.CharField(max_length=255, null=True)
    category_group = models.CharField(max_length=55, null=True)
    objects = models.Manager
