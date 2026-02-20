from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username',  'password']

    def create(self, validated_data):
        role = validated_data.pop('role', None)

        user = User.objects.create_user(**validated_data)

        if role:
            user.role = role
            user.save()

        return user
