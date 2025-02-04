from rest_framework import serializers
from django.contrib.auth import get_user_model  

User = get_user_model() 

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}  



# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         fields=('username','password')

#         extra_kword={
#              'username':{'required':True,'allow_blank':False},
#              'password':{'required':True,'allow_blank':False,'min_length':8}
           
#              }



# مشان معلومات المستخدم 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password') 



