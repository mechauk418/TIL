from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id","email")

class CustomUserRegisterSerializer(RegisterSerializer):

    def get_cleaned_data(self):
        super(CustomUserRegisterSerializer, self).get_cleaned_data()
        return {
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }

    def save(self, request):
        user = super().save(request)
        user.save()
        return user