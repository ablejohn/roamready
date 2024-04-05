import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from . import serializers, models
from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect


class SignUpView(View):
  def get(self, request):
    return render(request, "users/signup.html")
  
  def post(self, request):
    if request.method == "POST":
      first_name = request.POST.get("first_name")
      last_name = request.POST.get("last_name")
      email = request.POST.get("email")
      password = request.POST.get("password")
      username = email.split("@")[0]
      user = models.User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username)
      user.save()
      user.set_password(password)
      user.is_active = True
      user.save()
      return redirect("signin")
    return render(request, "users/signup.html")


class SignInView(View):
  def get(self, request):
    return render(request, "users/signin.html")

  def post(self, request):
    email =  request.POST.get("email")
    password = request.POST.get("password")
    username = email.split("@")[0]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect("/")
    return render(request, "users/signin.html")

def logout_view(request):
  logout(request)
  return redirect("/")

# @api_view(["POST",])
# def signup(request):
#   if request.method == "POST":
#     serializer = serializers.SignUpSerializers(data=request.data)
#     if serializer.is_valid():
#       user = serializer.save()
#       serializer = serializers.UserSerializer(user)
#       return Response(serializer.data)
    

# @api_view(["POST",])
# def signin(request):
#   if request.method == "POST":
#     serializer = serializers.SignInSerializers(data=request.data)
#     if serializer.is_valid():
#       email = serializer.validated_data["email"]
#       password = serializer.validated_data["password"]
#       username = email.split('@')[0]
#       user = authenticate(request, username=username, password=password)
#       serializer = serializers.UserSerializer(user)
#       if user is not None:
#         return Response({"data": "login successful", "user": serializer.data})
#       else:
#         return Response({"data": "invalid email or password"})
      

@api_view(["POST",])
def check_user(request):
  if request.method == 'POST':
    uid = request.data.get("uuid")
    if models.User.objects.filter(uuid=uid).exists():
      online =  True
    else:
      online = False
    return Response({"online": online})
  