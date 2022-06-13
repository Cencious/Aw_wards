from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    bio = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=120)
    profile_pic = CloudinaryField('image')
    # phone_number = PhoneField(max_length=15, blank=True)

    def __str__(self):
        