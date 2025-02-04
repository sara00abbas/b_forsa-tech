from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.login,name='register'),
    
    
]