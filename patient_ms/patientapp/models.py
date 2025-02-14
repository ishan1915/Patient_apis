from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rate = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)    