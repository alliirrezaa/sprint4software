from rest_framework import serializers
from ..models import Profile,User
from django.contrib.auth import get_user_model, logout
from django.contrib import auth

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['email','username','phone','password']
        extra_kwargs={
            'password':{'write_only':True},
            "username": {"error_messages": {"required": "نام کاربری را وارد کنید"}},
            "email": {"error_messages": {"required": "ایمیل را وارد کنید"}},
            "password": {"error_messages": {"required": "رمز عبور را وارد کنید"}},
            "phone": {"error_messages": {"required": "شماره تلفن را وارد کنید"}}
        }

    def save(self):
        user=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],
        )
        password1=self.validated_data['password']
        user.set_password(password1)
        user.save()
        return user

class ProfileHelperSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','username','phone']
        extra_kwargs={
            'email':{'read_only':True},
        }

class ProfileSerializer(serializers.ModelSerializer):
    user=ProfileHelperSerializer()
    name=serializers.CharField(required=False,allow_blank=True)
    last_name=serializers.CharField(required=False,allow_blank=True)
    phone2=serializers.IntegerField()
    province=serializers.CharField(required=False,allow_blank=True)
    address=serializers.CharField(required=False,allow_blank=True)
    class Meta:
        model=Profile
        fields=['user','name','last_name','phone2','province','address']

    def update(self, instance, validated_data):
        request = self.context.get("request")
        #get new data
        new_username=validated_data['user']['username']
        new_phone=validated_data['user']['phone']
        new_name = validated_data['name']
        new_last_name = validated_data['last_name']
        new_phone2=validated_data['phone2']
        new_province=validated_data['province']
        new_address= validated_data['address']
        #update User data
        user = request.user
        user.username=new_username
        user.phone=new_phone
        user.save()
        #update Profile data
        instance.name =new_name
        instance.last_name = new_last_name
        instance.phone2=new_phone2
        instance.province=new_province
        instance.address=new_address
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    