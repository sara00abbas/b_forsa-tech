
from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('auth/',include("devloper.urls"))
=======
    path('',include("devloper.urls"))
>>>>>>> 93ca1fc445c32d4d9f9d07f129e04d0deb8ec858
    
]
