
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse

from uprofile import models
from uprofile import forms


# Create your views here.
class BaseProfile(View):
    template_name = 'uprofile/create.html'

    def setup(self, *args, **kwargs) -> None:
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.context ={
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None
                ),
            }
        else:
            self.context ={
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None
                ),
            }


        self.render = render(self.request,self.template_name,self.context)
    

    def get(self, *args, **kwargs):
        return self.render

class CreateProfile(BaseProfile):
    def post(self, *args, **kwargs):
        return self.render

class UpdateProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update Profile')

class LoginProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login Profile')

class LogoutProfile(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout Profile')