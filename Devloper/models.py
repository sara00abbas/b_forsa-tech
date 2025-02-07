from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.core.validators import EmailValidator

class User(AbstractUser):
    email = models.EmailField(unique=True,null=True, blank=True )  
    username = models.CharField(max_length=150, unique=True,null=True, blank=True ) 
    password = models.CharField(max_length=128,null=True, blank=True)
    
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
    
    