from rest_framework import serializers
from . import models

class SignUpSerializers(serializers.Serializer):
  email = serializers.EmailField(required=True)
  first_name = serializers.CharField(required=True)
  last_name = serializers.CharField(required=True) 
  password = serializers.CharField(required=True)

  def save(self):
    email = self.validated_data["email"]
    first_name = self.validated_data["first_name"]
    last_name = self.validated_data["last_name"]
    password = self.validated_data["password"]
    username = email.split("@")[0]
    user = models.User.objects.create(email=email, first_name=first_name, last_name=last_name, username=username)
    user.save()
    user.set_password(password)
    user.is_active = True
    user.is_superuser = True
    user.save()
    return user

class SignInSerializers(serializers.Serializer):
  email = serializers.EmailField(required=True)
  password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = "__all__"
