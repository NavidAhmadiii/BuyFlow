from rest_framework import serializers
from rest_framework_simplejwt.tokens import TokenError, RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .models import Profile, CustomUser


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Incorrect phone number or password.")
        else:
            raise serializers.ValidationError("Both phone number and password are required.")

        return data


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('phone_number', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'profile_picture')


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    class Meta:
        fields = ('refresh',)

    def validate(self, attrs):
        refresh = attrs.get('refresh')
        refresh_token = RefreshToken(refresh)

        try:
            refresh_token.verify()
        except TokenError:
            # if refresh token is invalid or expire
            raise serializers.ValidationError({"error": "Invalid or expired refresh token"})

        # if the refresh token is valid , return refresh token itself
        attrs["refresh_token"] = refresh_token
        return attrs
