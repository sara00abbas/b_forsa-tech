
from django.contrib import admin
from django.urls import path
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("devloper.urls"))
    
]


