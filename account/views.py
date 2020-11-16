from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account
#from overtime.models import OvertimePerQtr
#from overtime.utils import getCurrentQtr
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from account.forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.
def logout_view(request):
    '''
    View used to log out users.
    '''
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def login_view(request):
    '''
    View used to login users.
    '''
    user = request.user
    if request.POST:
        login_form = AccountAuthenticationForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, "You have successfully logged in")
				#Functions to check leave allowance, ah submission and leave submissions placed here.
                return redirect("home_page")

    else:
        login_form = AccountAuthenticationForm()

    args = {'login_form': login_form}
    return render(request, "login_page.html", args)

@login_required()
def home_page(request):
    '''
    Views renders home page to user.
    '''
    return render(request, 'home_page.html')