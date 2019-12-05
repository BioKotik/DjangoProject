from django.db import models
from django.utils import timezone

# Create your models here.
class Record(models.Model):
    transaction = models.FloatField(max_length=30)
    category = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
