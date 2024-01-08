# authentication/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user profile if needed
class Registration(models.Model):
    user_name = models.CharField(max_length=100)
    email_reg = models.EmailField()
    password_reg= models.CharField(max_length=50)