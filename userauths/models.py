
from django.db import models
from django.contrib.auth.models import AbstractUser


from shortuuid.django import ShortUUIDField
from PIL import Image


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


class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=255, alphabet="qwertyuiopasdfghjklzxcvbnm1234567890")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    images = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255, null=True, blank=True, blank=True) 
    city = models.CharField(max_length=255, null=True, blank=True, blank=True) 
    country = models.CharField(max_length=255, null=True, blank=True, blank=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

