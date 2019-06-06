from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Times(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeframe = models.TextField()
    description = models.TextField()
    save_time = models.TimeField()