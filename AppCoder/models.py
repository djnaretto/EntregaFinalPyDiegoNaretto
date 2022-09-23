from django.db import models
from django.contrib.auth.models import User
from datetime import *

# Create your models here.

#Post
class Post(models.Model):
    title= models.CharField(max_length=50)
    subtitle= models.CharField(max_length=100)
    image= models.ImageField(upload_to='images', null=True, blank=True)
    author= models.CharField(max_length=50)
    date= models.DateField(auto_now_add=True)
    text= models.TextField()

    def __str__(self):
        return f"Title: {self.title} - Author {self.author} - Date {self.date}"

#Avatar
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='avatares', null=True, blank=True)