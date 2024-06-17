
from django.forms import ModelForm
from django.contrib.auth.models import User
from uprofile import models

class ProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ('user',)
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email')
    
    def clean(self,*args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        
