from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import post_save

from PIL import Image
from shortuuid.django_fields import ShortUUIDField

import shortuuid

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
    address = models.CharField(max_length=255, null=True, blank=True) 
    city = models.CharField(max_length=255, null=True, blank=True) 
    country = models.CharField(max_length=255, null=True, blank=True)
    verified = models.BooleanField(default=False)
    slug = models.SlugField(unique=True ,null=True ,blank=True)
    
    def __str__(self):
        if self.username != "" or self.username != None:
            return self.username
        else:
            return self.user.username
    
    # import shortuuid
    def save(self, *args , **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()   # user_name-bbnmbvcfxgfhfjgtfrqwertyhbfdsdfgdfvgb
            uniqueid = uuid_key[:10]    # user_qw
            self.slug = slugify(self.username) + '-' + str(uniqueid.lower()) #islam-hamdy-qwer
        super(Profile, self).save(*args, **kwargs)

# create user profile automatic
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
