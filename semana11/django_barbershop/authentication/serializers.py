from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'last_login')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'last_login')
        read_only_fields = ('status',)

    def save(self):
        instance = self.instance
        validated_data = self.validated_data

        if instance:
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.role = validated_data.get('role', instance.role)

            if 'password' in validated_data:
                instance.set_password(validated_data.get('password'))

            instance.save()
            return instance
        else:
            user = User(**validated_data)
            user.set_password(validated_data.get('password'))
            user.save()
            return user
        
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        user = authenticate(**authenticate_kwargs)

        if user and user.status:
            return super().validate(attrs)
        
        raise serializers.ValidationError('Invalid email or password')
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['role'] = user.role.name
        return token