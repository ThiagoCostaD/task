from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        allow_blank=False,
        allow_null=False,
    )
    password = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        write_only=True,
    )

    def validate(self, data):
        user = authenticate(**data)
        if user:
            if user.is_active:
                return user
            raise serializers.ValidationError('Account is inactive.')
        raise serializers.ValidationError('Invalid login credentials.')


class EditTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        extra_kwargs = {'completed': {'required': False}}
        permission_classes = (IsAuthenticated,)


class DeleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        extra_kwargs = {'completed': {'required': False}}
        permission_classes = (IsAuthenticated,)


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']
        extra_kwargs = {'completed': {'required': False}}
        permission_classes = (IsAuthenticated,)
        owner = serializers.ReadOnlyField(source='owner.username')

        title = serializers.CharField(
            max_length=150,
            required=True,
            allow_blank=False,
            allow_null=False,
        )

        description = serializers.CharField(
            required=True,
            allow_blank=False,
            allow_null=False,
        )

        completed = serializers.BooleanField(
            required=False,
        )

        due_date = serializers.DateField(
            required=False,
        )


class LogoutSerializer(serializers.Serializer):
    def logout(self, request):
        request.user.auth_token.delete()
        return None
