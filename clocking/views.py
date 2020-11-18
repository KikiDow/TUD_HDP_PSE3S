from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from .models import Quarter, Shift, RosterSideA, RosterSideB, Roster
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

@login_required()
def generate_roster(request, pk):
    '''
    This view creates a roster for a newly created user.
    '''
    roster_start_point = findRosterStartPoint()
    roster_pointer = roster_start_point
    date_pointer = datetime.date.today()
    one_day_delta = datetime.timedelta(days=1)
    officer_for_roster_being_generated = get_object_or_404(Account, pk=pk)
    officer_for_roster_being_generated_id = officer_for_roster_being_generated.pk
    officers_roster_side = officer_for_roster_being_generated.roster_side
    while_counter = 0
    while(while_counter < 731):
        roster_pointer = rosterPointerCheck(roster_pointer)
        
        if officers_roster_side == "A":
            schedule_pointer = RosterSideA.objects.get(ros_a_shift_cycle_number=roster_pointer) #check syntax
            label_for_shift_on_that_day = schedule_pointer.ros_a_shift_label
            if label_for_shift_on_that_day == "Off":
                dueOn_or_dueOff = schedule_pointer.ros_a_due_on
            else:
                shift_for_that_day = Shift.objects.get(shift_label=label_for_shift_on_that_day)
                dueOn_or_dueOff = schedule_pointer.ros_a_due_on
        else:
            schedule_pointer = RosterSideB.objects.get(ros_b_shift_cycle_number=roster_pointer)
            label_for_shift_on_that_day = schedule_pointer.ros_b_shift_label
            if label_for_shift_on_that_day == "Off":
                dueOn_or_dueOff = schedule_pointer.ros_b_due_on
            else:
                shift_for_that_day = Shift.objects.get(shift_label=label_for_shift_on_that_day)
                dueOn_or_dueOff = schedule_pointer.ros_b_due_on
        
        if label_for_shift_on_that_day == "Off":
            new_roster_record = Roster(roster_officer_id=officer_for_roster_being_generated, roster_shift_label=label_for_shift_on_that_day, roster_shift_date=date_pointer, roster_due_on=dueOn_or_dueOff)
        else:
            new_roster_record = Roster(roster_officer_id=officer_for_roster_being_generated, roster_shift_label=label_for_shift_on_that_day, roster_shift=shift_for_that_day, roster_shift_date=date_pointer, roster_due_on=dueOn_or_dueOff)
        
        new_roster_record.save()
        print(new_roster_record)
        roster_pointer += 1
        date_pointer = date_pointer + one_day_delta
        while_counter = Roster.objects.filter(roster_officer_id=officer_for_roster_being_generated.pk).count()
        print(while_counter)
    
    return redirect('home_page')