from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from .models import Quarter, Shift, RosterSideA, RosterSideB, Roster, PersonalDetails
from .forms import PersonalDetailsForm
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
    
    messages.success(request, "Roster created for new account.")
    return redirect('home_page')
    
@login_required()
def view_personal_details(request):
    '''
    This view allows the user to view their personal details. It checks whether the user has yet created the personal details and then initialised the context variables approporiately.
    '''
    user = request.user
    personal_details_check = PersonalDetails.objects.filter(officer_pd=user)

    if personal_details_check.exists():
        personal_details = PersonalDetails.objects.get(officer_pd=user)
        info_message = ""
        personal_details_exist = True
    else:
        info_message = "You have not yet filled out any personal details. Select the button below to begin."
        personal_details_exist = False
        personal_details = None
        
    args = {'personal_details': personal_details, 'info_message': info_message, 'personal_details_exist': personal_details_exist}
    return render(request, "view_personal_details.html", args)
    
@login_required()
def create_personal_details(request):
    '''
    This view present the personal details form to the user allwing them to create their personal details.
    '''
    if request.method == "POST":
        create_personal_details_form = PersonalDetailsForm(request.POST, request.FILES)
        if create_personal_details_form.is_valid():
            create_personal_details_form.instance.officer_pd = request.user
            personal_details = create_personal_details_form.save()
            messages.success(request, 'You have successfully filled out your personal details.')
            
            args = {'personal_details': personal_details}
            return redirect(view_personal_details)
    else:
        create_personal_details_form = PersonalDetailsForm()
        
    return render(request, "create_personal_details.html", {'create_personal_details_form': create_personal_details_form})
    
@login_required()
def edit_personal_details(request, pk):
    """
    This view allows the user to update any changes in their personal details.
    """
    personal_details = get_object_or_404(PersonalDetails, pk=pk) if pk else None
    user = request.user
    if request.method == "POST":
        edit_personal_details_form = PersonalDetailsForm(request.POST, request.FILES, instance=personal_details)
        if edit_personal_details_form.is_valid():
            edit_personal_details_form.instance.officer_pd = request.user
            personal_details = edit_personal_details_form.save()
            messages.success(request, 'You have successfully updated your personal details.')

            return redirect(view_personal_details)
    else:
        edit_personal_details_form = PersonalDetailsForm(instance=personal_details)
        

    return render(request, "edit_personal_details.html", {'personal_details': personal_details, 'edit_personal_details_form': edit_personal_details_form})
    
