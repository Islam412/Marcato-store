from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image
from shortuuid.django_fields import ShortUUIDField

import shortuuid

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER)
    
    otp = models.CharField(max_length=255, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=255, alphabet="qwertyuiopasdfghjklzxcvbnm1234567890")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    images = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255, null=True, blank=True) 
    city = models.CharField(max_length=255, null=True, blank=True) 
    country = models.CharField(max_length=255, null=True, blank=True)
    verified = models.BooleanField(default=False)
    slug = models.SlugField(unique=True ,null=True ,blank=True)
    
    def __str__(self):
        return self.username or self.user.email
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(f'{self.first_name}-{self.last_name}')
        if not self.slug:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:10]
            self.slug = slugify(self.username) + '-' + str(uniqueid.lower())
        super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
