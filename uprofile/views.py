from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.
class CreateProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Create Profile')

class UpdateProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update Profile')

class LoginProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login Profile')

class LogoutProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout Profile')