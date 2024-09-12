from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie_Model(models.Model):
    movie_name = models.CharField(max_length=150)
    discription = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE) 
    
    
    
    
    