from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'accounts/index.html')
	

def register_page(request):
	return render(request, 'accounts/register.html')


def login_page(request):
	return render(request, 'accounts/login.html')


