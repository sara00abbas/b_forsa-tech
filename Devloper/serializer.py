from rest_framework import serializers
from django.contrib.auth import get_user_model  # استخدام النموذج المخصص

User = get_user_model()  # اجلب نموذج المستخدم الحالي

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # لا تعرض كلمة المرور في الرد
<<<<<<< HEAD
=======



# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         fields=('username','password')

#         extra_kword={
#              'username':{'required':True,'allow_blank':False},
#              'password':{'required':True,'allow_blank':False,'min_length':8}
           
#              }
>>>>>>> 93ca1fc445c32d4d9f9d07f129e04d0deb8ec858






# 



