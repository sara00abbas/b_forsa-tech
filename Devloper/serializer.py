from rest_framework import serializers
from django.contrib.auth import get_user_model  # استخدام النموذج المخصص

User = get_user_model()  # اجلب نموذج المستخدم الحالي

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # لا تعرض كلمة المرور في الرد






# 



