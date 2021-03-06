from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
import datetime
from clocking.models import Quarter
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account
from overtime.models import OvertimePerQtr
from overtime.utils import getCurrentQtr
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from account.forms import RegistrationForm, AccountAuthenticationForm
from notifications.signals import notify

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
    
@login_required
def registration(request):
    '''
    This view renders the user registration form for users 
    '''
    if request.POST:
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            email = reg_form.cleaned_data.get('email')
            raw_password = reg_form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            new_account = Account.objects.get(email=email)
            notify.send(request.user, recipient=new_account, verb="Can you please fill in your personal details as soon as possible.")
            messages.success(request, "You have successfully registered a new user.")
            current_qtr = getCurrentQtr()
            new_ot_per_qtr = OvertimePerQtr(ot_per_qtr_off_id=new_account, ot_per_qtr_qtr_id=current_qtr)
            new_ot_per_qtr.save()
            
            return redirect('view_new_account', new_account.pk)
            
    else:
        reg_form = RegistrationForm()
    
    args = {'reg_form': reg_form}
    return render(request, 'register.html', args)
    
@login_required()
def view_new_account(request, pk):
    '''
    This view shows a supervisor user the user they have just created with options to delete or edit the user.
    '''
    newly_created_account = get_object_or_404(Account, pk=pk)
    newly_created_account.save()
    return render(request, 'view_new_account.html', {'newly_created_account': newly_created_account})
    
@login_required()
def delete_account(request, pk):
    '''
    This view allows supervisor users to delete an account.
    '''
    account_for_deletion = Account.objects.get(pk=pk)
    account_for_deletion.delete()
    messages.success(request, "You have successfully deleted this account.")
    return redirect('registration')
    
@login_required()
def edit_new_account(request, pk):
    '''
    This view allows a supervisor user to edit an account they have just created. Incase of errors.
    '''
    account_for_editing = get_object_or_404(Account, pk=pk) if pk else None
    if request.method == "POST":
        edit_account_form = RegistrationForm(request.POST, request.FILES, instance=account_for_editing)
        if edit_account_form.is_valid():
            account_for_editing = edit_account_form.save()
            messages.success(request, 'You have successfully made changes to this account.')
            return redirect(view_new_account, account_for_editing.pk)
    else:
        edit_account_form = RegistrationForm(instance=account_for_editing)
        

    return render(request, "edit_new_account.html", {'account_for_editing': account_for_editing, 'edit_account_form': edit_account_form})
    
@login_required()
def generate_quarters(request):
    '''
        This view allows the superuser to generate two years worth of quarters.
    '''
    date_1 = settings.GLOBAL_START_DATE
    one_day_delta = datetime.timedelta(days=1)
    quarter_delta = datetime.timedelta(days=90)
    base_label = "Qtr"
    label_qtr_number = 1
    counter = 0
    while(counter < 16):
        qtr_start = date_1
        qtr_end = qtr_start + quarter_delta
        new_qtr_label = base_label + str(label_qtr_number)
        new_quarter = Quarter(qtr_start_date=qtr_start, qtr_end_date=qtr_end, qtr_label=new_qtr_label)
        new_quarter.save()
        #Used for testing.
        print(new_qtr_label + ":")
        print("Qtr Start: " + str(qtr_start))
        print("Qtr End : " + str(qtr_end))
        #Reseting while loop variables.
        date_1 = qtr_end + one_day_delta
        label_qtr_number += 1
        counter = Quarter.objects.count()
        
    if counter == 15:
        messages.success(request, "You have successfully generated new quarters.")
    
    return redirect('home_page')