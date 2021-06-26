from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from  PIL import Image

# Create your models here.

class Contact(models.Model):
    #database table name
    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=None)
    phone = models.CharField(max_length=13, default=None)
    email = models.EmailField(max_length=100, default=None)
    msg = models.TextField(max_length=5000, default=None)
    country = models.TextField(max_length=50, default=None)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    #showing sender name without pressing the message
    def __str__(self):
        return  self.name + '-' + '(' + self.email + ')'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.CharField(max_length=100, null=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    country = models.TextField(max_length=50, null=True, blank=True)
    city  = models.TextField(max_length=50, null=True, blank=True)
    gender  = models.CharField(max_length=7, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)



    def __str__(self):
        return f'{self.user.username} Profile'

    #fixed Image Size 
    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail (output_size)
            img.save(self.image.path)