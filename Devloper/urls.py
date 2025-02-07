from django.urls import path
from . import views

urlpatterns = [ 
    path('signUp/',views.register,name='register'),
      
]