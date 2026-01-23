from rest_framework import serializers
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