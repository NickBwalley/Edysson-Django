from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.conf import settings

# Create your views here.
from .forms import *
from .models import *
from .decorators import *

def home(request):
	return render(request, 'accounts/index.html')
	


def register_page(request):
	form = create_user_form()

	if request.method == 'POST':
		form = create_user_form(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username') # allows to get only the username without any other details
			messages.success(request, 'Account successfully created for: ' + user)
			return redirect('login')

	context = {'form':form}
	return render(request, 'accounts/register.html', context)



def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Incorrect Username or Password!')

	context = {}
	return render(request, 'accounts/login.html', context)

@unauthenticated_user
def dashboard(request):
	return render(request, 'accounts/dashboard.html', context)