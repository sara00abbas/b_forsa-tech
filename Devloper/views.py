from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializer import SingUpSerializer

<<<<<<< HEAD
User = get_user_model()  
=======
User = get_user_model()  # استخدام نموذج المستخدم المخصص
>>>>>>> 93ca1fc445c32d4d9f9d07f129e04d0deb8ec858

@api_view(['POST'])
def login(request):
    data = request.data
    
<<<<<<< HEAD
    
=======
    # التحقق من صحة البيانات باستخدام Serializer
>>>>>>> 93ca1fc445c32d4d9f9d07f129e04d0deb8ec858
    serializer = SingUpSerializer(data=data)
    if serializer.is_valid():
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

<<<<<<< HEAD
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'This email already exists!'}, status=status.HTTP_400_BAD_REQUEST)

       
        user = User.objects.create(
            email=email,
            username=username,
            password=make_password(password),  
=======
        # التحقق مما إذا كان المستخدم موجودًا بالفعل
        if User.objects.filter(email=email).exists():
            return Response({'error': 'This email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # إنشاء المستخدم الجديد
        user = User.objects.create(
            email=email,
            username=username,
            password=make_password(password),  # تأكد من تشفير كلمة المرور
>>>>>>> 93ca1fc445c32d4d9f9d07f129e04d0deb8ec858
        )

        return Response({'details': 'Your account registered successfully'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
