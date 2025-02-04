from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    # fcm_token = models.CharField(max_length=2000, blank=True, null=True)


    def __str__(self):
        return self.email  
    

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
