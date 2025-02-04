from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.core.validators import EmailValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)  
    username = None  

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email