from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Users, Cars, Clients, Orders


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username")
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = 'User account is deactivated.'
                    raise serializers.ValidationError(msg)
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'passport_series', 'firstname', 'lastname', 'phone']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'brand', 'model']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'client_id', 'car_id', 'timestamp']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password']
