from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(default=True)
    is_superuser = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=True)
    
    class Meta: 
        model = get_user_model()
        fields = ['id','password', 'email', 'company_reg_number','is_active', 'is_superuser', 'is_staff', 'date_joined', 'last_login']
        
    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        password = validated_data.pop('password')
        user.set_password(password)
        user.save()
        return user
        
        
        
       