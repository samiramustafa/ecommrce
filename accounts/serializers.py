from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profail
from django.contrib.auth.hashers import make_password


# class Profaol_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Profail
#         fields=[]



class SingUp_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')
        #  validation
        extra_kwargs={'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.password = make_password(validated_data['password'])
        user.save()
        return user

    
        #     'first_name':{'required':True,  'allow_blank':False},
        #     'last_name':{'required':True,  'allow_blank':False},
        #     'username':{'required':True, 'allow_blank':False},
        #     'email':{'required':True, 'allow_blank':False},
        #     'password':{'required':True,  'allow_blank':False,'min_length':8, 'write_only': True},
#محتاجه اهيش الباسورد وعمل فاليديشن يقبل ارقم
# فى مشكله فى ال token
# user info back
# class User_serializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('first_name','username','email','password')