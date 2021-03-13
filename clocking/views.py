from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from .models import Quarter, Shift, RosterSideA, RosterSideB, Roster, PersonalDetails, ManualClocking
from .forms import PersonalDetailsForm, ManualClockingForm, RejectManualClockingForm
from django.contrib import messages
from.utils import findRosterStartPoint, rosterPointerCheck, getStartPageForPagination, getSearchResultPaginationStartPage, convertStrToDateObj
from account.models import Account
from notifications.signals import notify
from notifications.models import Notification
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def landing_page(request):
    '''
    A view that renders the landing page of the application.
    '''
    return render(request, "landing_page.html")

@login_required()
def clocking_page(request):
    user = request.user
    first_record = Roster.objects.filter(roster_officer_id=user).first()
    first_day_of_users_roster = first_record.roster_shift_date
    users_roster = Roster.objects.filter(roster_officer_id=user).order_by('id')
    #Pagination
    page_number = getStartPageForPagination(first_day_of_users_roster)
    page = request.GET.get('page', page_number)
    
    paginator = Paginator(users_roster, 7)
    try:
        users_ros = paginator.page(page)
    except PageNotAnInteger:
        users_ros = paginator.page(1)
    except EmptyPage:
        users_ros = paginator.page(paginator.num_pages)
        
    return render(request, 'clocking_page.html', {'users_ros': users_ros})
    
def search_roster(request):
    user = request.user
    first_record = Roster.objects.filter(roster_officer_id=user).first()
    first_day_of_users_roster = first_record.roster_shift_date
    users_roster = Roster.objects.filter(roster_officer_id=user).order_by('id')
    
    search_date = request.GET['q']
    #print(search_date)
    date_as_obj = convertStrToDateObj(search_date)
    
    page_number = getSearchResultPaginationStartPage(first_day_of_users_roster, date_as_obj)
    
    page = request.GET.get('page', page_number)
    
    paginator = Paginator(users_roster, 7)
    try:
        users_ros = paginator.page(page)
    except PageNotAnInteger:
        users_ros = paginator.page(1)
    except EmptyPage:
        users_ros = paginator.page(paginator.num_pages)
        
    return render(request, "roster_search_result.html", {'users_ros': users_ros})
'''
@login_required()
def generate_quarters(request):
    #This view allows the superuser to generate two years worth of quarters.
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
'''

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
    This view allows the user to view their personal details. It checks whether the user has yet created the 
    personal details and then initialised the context variables approporiately.
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
    
@login_required()    
def my_notifications(request):
    """
    This view will render the notifications page showing the user their unread notifications.
    """

    user = request.user.id
    notifications = Notification.objects.unread().filter(recipient=user).order_by('-timestamp')
    return render(request, "notifications.html", {'notifications': notifications})
    
@login_required()
def clock(request):
    user = request.user
    todays_date = datetime.date.today()
    roster_record_for_today = Roster.objects.get(roster_officer_id=user, roster_shift_date=todays_date)
    roster_record_for_today.updateCorrectClocking(request)
    roster_record_for_today.save()
    return redirect("home_page")
    
@login_required()
def manual_clocking(request):
    if request.method == "POST":
        manual_clock_form = ManualClockingForm(request.POST, request.FILES)
        if manual_clock_form.is_valid():
            manual_clock_form.instance.mc_officer_id = request.user
            manual_clock = manual_clock_form.save()
            messages.success(request, 'You have successfully submitted a manual clocking form.')
            return redirect(view_manual_clock, manual_clock.pk)
    else:
        manual_clock_form = ManualClockingForm()
    return render(request, "submit_manual_clocking_form.html", {'manual_clock_form': manual_clock_form})
    
@login_required()
def view_manual_clock(request, pk):
    manual_clock = get_object_or_404(ManualClocking, pk=pk)
    manual_clock.save()
    return render(request, "view_manual_clock.html", {'manual_clock': manual_clock})
    
@login_required()
def view_submitted_manual_clockings(request):
    user = request.user
    submitted_manual_clockings = ManualClocking.objects.filter(checked_by_validator=False).exclude(mc_officer_id=user)
    length_staff_manual_clockings = len(submitted_manual_clockings)
    return render(request, "view_submitted_manual_clockings.html", {'submitted_manual_clockings': submitted_manual_clockings, 'length_staff_manual_clockings': length_staff_manual_clockings})
    
@login_required()
def accept_manual_clock(request, pk):
    manual_being_accepted = ManualClocking.objects.get(pk=pk)
    manual_being_accepted.accept_reject_clock = True
    manual_being_accepted.checked_by_validator = True
    manual_being_accepted.validator_id = request.user
    manual_being_accepted.save()
    
    roster_record_for_manual_clock = Roster.objects.get(roster_officer_id=manual_being_accepted.mc_officer_id, roster_shift_date=manual_being_accepted.clocking_date)
    roster_record_for_manual_clock.clocking_in_time = manual_being_accepted.clocking_in_time
    roster_record_for_manual_clock.lunch_out_time = manual_being_accepted.lunch_out_time
    roster_record_for_manual_clock.lunch_in_time = manual_being_accepted.lunch_in_time
    roster_record_for_manual_clock.clocking_out_time = manual_being_accepted.clocking_out_time
    roster_record_for_manual_clock.save()
    
    notify.send(request.user, recipient=manual_being_accepted.mc_officer_id, verb=" accepted your manual clocking entry for " + str(manual_being_accepted.clocking_date))
    messages.success(request, 'Manual Clock Accepted')
    return redirect("view_submitted_manual_clockings")
    
@login_required()
def reject_manual_clock(request, pk):
    manual_clock_being_rejected = ManualClocking.objects.get(pk=pk)
    if request.method == "POST":
        manual_clock_reject_form = RejectManualClockingForm(request.POST, request.FILES, instance=manual_clock_being_rejected)
        if manual_clock_reject_form.is_valid:
            manual_clock_being_rejected = manual_clock_being_rejected.save()
            manual_clock_being_rejected.accept_reject_clock = False
            manual_clock_being_rejected.checked_by_validator = True
            manual_clock_being_rejected.validator_id = request.user
            manual_clock_being_rejected.save()
            notify.send(request.user, recipient=manual_clock_being_rejected.mc_officer_id, verb=" rejected your manual clocking entry for " + str(manual_clock_being_rejected.clocking_date))
            messages.success(request, 'Manual Clock Rejected')
    else:
        manual_clock_reject_form = RejectManualClockingForm(instance=manual_clock_being_rejected)
    return render(request, "reject_manual_clock.html", {'manual_clock_being_rejected': manual_clock_being_rejected, 'manual_clock_reject_form': manual_clock_reject_form})
    
@login_required()
def previous_manual_clockings(request):
    user = request.user
    user_manual_clocks = ManualClocking.objects.filter(mc_officer_id=user).order_by('-clocking_date')
    len_manual_clocks = len(user_manual_clocks)
    page = request.GET.get('page', 1)
    
    paginator = Paginator(user_manual_clocks, 8)
    try:
        my_manual_clocks = paginator.page(page)
    except PageNotAnInteger:
        my_manual_clocks = paginator.page(1)
    except EmptyPage:
        my_manual_clocks = paginator.page(paginator.num_pages)
    
    return render(request, "previous_manual_clockings.html", {'my_manual_clocks': my_manual_clocks, 'len_manual_clocks': len_manual_clocks})
    
@login_required()
def search_manual_clocks(request):
    user = request.user
    mc_search_date = request.GET['q']
    date = convertStrToDateObj(mc_search_date)
    mc_search_result = ManualClocking.objects.filter(mc_officer_id=user, clocking_date=date)
   
    page = request.GET.get('page', 1)
    
    paginator = Paginator(mc_search_result, 8)
    try:
        my_manual_clocks = paginator.page(page)
    except PageNotAnInteger:
        my_manual_clocks = paginator.page(1)
    except EmptyPage:
        my_manual_clocks = paginator.page(paginator.num_pages)
    
    return render(request, "manual_clock_search.html", {'my_manual_clocks': my_manual_clocks})
    
@login_required()
def edit_manual_clock(request, pk):
    '''
    View in combination with conditional content on view_manual_clock.html allows a user to edit a previously
    submitted manual clocking before it is checked by a validator.
    '''
    manual_clock_for_editing = get_object_or_404(ManualClocking, pk=pk) if pk else None
    if request.method == "POST":
        edit_manual_clock_form = ManualClockingForm(request.POST, request.FILES, instance=manual_clock_for_editing)
        if edit_manual_clock_form.is_valid():
            manual_clock_for_editing = edit_manual_clock_form.save()
            messages.success(request, 'You have successfully made changes to this manual clocking.')
            return redirect(view_manual_clock, manual_clock_for_editing.pk)
    else:
        edit_manual_clock_form = ManualClockingForm(instance=manual_clock_for_editing)
    return render(request, "edit_manual_clock.html", {'manual_clock_for_editing': manual_clock_for_editing, 'edit_manual_clock_form': edit_manual_clock_form})
    
@login_required()
def delete_manual_clock(request, pk):
    '''
    View allows user to delete one of their own manual clockings.
    '''
    manual_clock__for_deletion = ManualClocking.objects.get(pk=pk)
    manual_clock__for_deletion.delete()
    messages.success(request, "You have successfully deleted this Manual Clocking.")
    return redirect('previous_manual_clockings')