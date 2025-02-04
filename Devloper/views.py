from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializer import SingUpSerializer

User = get_user_model()  # استخدام نموذج المستخدم المخصص

@api_view(['POST'])
def register(request):
    data = request.data
    
    # التحقق من صحة البيانات باستخدام Serializer
    serializer = SingUpSerializer(data=data)
    if serializer.is_valid():
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        # التحقق مما إذا كان المستخدم موجودًا بالفعل
        if User.objects.filter(email=email).exists():
            return Response({'error': 'This email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # إنشاء المستخدم الجديد
        user = User.objects.create(
            email=email,
            username=username,
            password=make_password(password),  # تأكد من تشفير كلمة المرور
        )

        return Response({'details': 'Your account registered successfully'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
