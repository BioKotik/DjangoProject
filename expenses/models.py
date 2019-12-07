from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Record(models.Model):
    transaction = models.FloatField(max_length=30)
    category = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='all_records')

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    birthday = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Profile for {}'.format(self.user.username)
