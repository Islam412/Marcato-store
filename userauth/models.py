from django.db import models
from django.contrib.auth.models import AbstractUser



GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class User(AbstractUser):
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER)
    
    otp = models.CharField(max_length=255, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username

    