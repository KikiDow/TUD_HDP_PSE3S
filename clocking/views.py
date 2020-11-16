from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from .models import Quarter
# models from line above: to be restored once models created and migrated: Shift, RosterSideA, RosterSideB, Roster
from django.contrib import messages
from.utils import findRosterStartPoint, rosterPointerCheck
from account.models import Account
# Create your views here.

def landing_page(request):
    '''
    A view that renders the landing page of the application.
    '''
    return render(request, "landing_page.html")

@login_required()
def clocking_page(request):
    return render(request, 'clocking_page.html')   
    
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
    while(counter < 10):
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
        
    if counter == 9:
        messages.success(request, "You have successfully generated new quarters.")
    
    return redirect('home_page')
