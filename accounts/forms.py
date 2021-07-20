from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms
from .models import *

class create_user_form(UserCreationForm):
	class Meta:
		model = user
		fields = ['username', 'email', 'country']
		

# class update_user_profile(forms.ModelForm):
# 	class Meta:
# 		model = user
# 		fields = ['username', 'phonenumber', 'country', 'profile_pic', 'bio', 'hide_email', 'hide_phonenumber']
# 		exclude = ['email', 'university', 'course', 'password1', 'password2']
		