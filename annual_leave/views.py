from django.shortcuts import render, redirect, get_object_or_404
from .utils import getCurrentYear, getLeaveAmount
from .models import AnnualLeave, AnnualLeaveRequest, ShortTermAnnualLeaveRequest
import datetime
from django.contrib.auth.decorators import login_required
from .forms import AnnualLeaveRequestForm, ShortTermAnnualLeaveRequestForm, AnnualLeaveRequestRejectForm, ShortTermLeaveRequestRejectForm
from django.contrib import messages
from account.models import Account
from itertools import chain
from clocking.models import Roster, Shift
from notifications.signals import notify

# Create your views here.
@login_required()
def annual_leave_page(request):
    '''
    This view renders the annual leave page to the user, showing the users upcoming leave and providing links to request leave
    and view previous leave requests.
    '''
    current_year = getCurrentYear()
    officer_user = request.user
    off = Account.objects.get(pk=officer_user.pk)
    off_current_leave_total = off.current_leave_total
    officers_leave = AnnualLeave.objects.filter(al_officer_id=officer_user.pk).filter(al_date__year=current_year)
    todays_date = datetime.date.today()
    upcoming_leave = []
    previous_leave = []
    for leave in officers_leave:
        if leave.al_date <= todays_date:
            previous_leave.append(leave)
        else:
            upcoming_leave.append(leave)
            
    length_upcoming_leave = len(upcoming_leave)
    length_previous_leave = len(previous_leave)
    
    return render(request, "annual_leave.html", {'upcoming_leave': upcoming_leave, 'previous_leave': previous_leave, 'length_previous_leave': length_previous_leave, 'length_upcoming_leave': length_upcoming_leave, 'off_current_leave_total': off_current_leave_total})

# BLOCK LEAVE
@login_required()
def block_leave_request(request):
    '''
    This view allows the user to submit a block leave request.
    '''
    if request.method == "POST":
        block_leave_form = AnnualLeaveRequestForm(request.POST, request.FILES)
        if block_leave_form.is_valid():
            block_leave_form.instance.al_request_officer_id = request.user
            #
            leave_requested_start = block_leave_form.instance.leave_request_start_date
            leave_requested_end = block_leave_form.instance.leave_request_last_date
            leave_hours_requested = 0.0
            one_day_delta = datetime.timedelta(days=1)
            adjusted_requested_end_date = leave_requested_end + one_day_delta
            list_of_requested_leave_dates = []
    
            for i in range((adjusted_requested_end_date - leave_requested_start).days):
                a_date = (leave_requested_start + datetime.timedelta(days=i))
                list_of_requested_leave_dates.append(a_date)
    
            for date in list_of_requested_leave_dates:
                leave_requested_date = Roster.objects.get(roster_shift_date=date, roster_officer_id=block_leave_form.instance.al_request_officer_id)
                if leave_requested_date.roster_due_on == True:
                    shift = Shift.objects.get(shift_label=leave_requested_date.roster_shift_label)
                    shift_hours = shift.shift_duration
                    leave_hours_requested += shift_hours
                    
            officers_leave_remaining = block_leave_form.instance.al_request_officer_id.current_leave_total
                    
            if block_leave_form.instance.leave_request_start_date > block_leave_form.instance.leave_request_last_date:
                messages.error(request, "The requested start date must be before the last requested date.")
                return render(request, "submit_block_leave.html", {'block_leave_form': block_leave_form})
            elif leave_hours_requested > officers_leave_remaining:
                messages.error(request, "You do not have enough leave remaining to make this request.")
                return render(request, "submit_block_leave.html", {'block_leave_form': block_leave_form})
            else:
                block_leave = block_leave_form.save()
                messages.success(request, 'You have successfully submitted an annual leave request.')
                return redirect(view_annual_leave_request, block_leave.pk)
    else:
        block_leave_form = AnnualLeaveRequestForm()
    return render(request, "submit_block_leave.html", {'block_leave_form': block_leave_form})
    
@login_required()
def view_annual_leave_request(request, pk):
    '''
    This view renders a specific annual leave request.
    '''
    annual_leave_req = get_object_or_404(AnnualLeaveRequest, pk=pk)
    applicants_leave_balance = annual_leave_req.al_request_officer_id.current_leave_total
    annual_leave_req.save()
    return render(request, "view_al_request.html", {'annual_leave_req': annual_leave_req, 'applicants_leave_balance': applicants_leave_balance})
    
@login_required()
def delete_block_leave_request(request, pk):
    '''
    This view in combination with conditional content on the view annual leave request page allows a user to delete one of their 
    block leave requests.
    '''
    block_leave_request_for_deletion = AnnualLeaveRequest.objects.get(pk=pk)
    block_leave_request_for_deletion.delete()
    messages.success(request, "You have successfully deleted this block leave request.")
    return redirect('annual_leave_page')
    
@login_required()
def edit_block_leave_request(request, pk):
    '''
    This view along with conditional content allows a user to edit a block leave request prior to it being checked by a 
    validator. Thsi view handles the server side validation.
    '''
    bl_request_for_editing = get_object_or_404(AnnualLeaveRequest, pk=pk) if pk else None
    if request.method == "POST":
        edit_bl_request_form = AnnualLeaveRequestForm(request.POST, request.FILES, instance=bl_request_for_editing)
        if edit_bl_request_form.is_valid():
            bl_request_for_editing = edit_bl_request_form.save()
            messages.success(request, 'You have successfully made changes to this annual leave request.')
            return redirect(view_annual_leave_request, bl_request_for_editing.pk)
    else:
        edit_bl_request_form = AnnualLeaveRequestForm(instance=bl_request_for_editing)
    return render(request, "edit_al_request.html", {'bl_request_for_editing': bl_request_for_editing, 'edit_bl_request_form': edit_bl_request_form})

#SHORT TERM LEAVE
@login_required()
def short_term_leave_request(request):
    '''
    This view manages a short term annual leave request. It contain server side validation.
    '''
    if request.method == "POST":
        short_term_leave_form = ShortTermAnnualLeaveRequestForm(request.POST, request.FILES)
        if short_term_leave_form.is_valid():
            #Place the user id into the foreign key field placeholder for the officer requesting leave. 
            short_term_leave_form.instance.st_annual_leave_request_officer_id = request.user
            #The next four lines of code instantiates the variables that will be used to check if the officer has enough leave remaining to make the request.  
            start_time_date_leave_amount_check = datetime.datetime.combine(short_term_leave_form.instance.st_leave_date, short_term_leave_form.instance.st_leave_start_time)
            finish_time_date_leave_amount_check = datetime.datetime.combine(short_term_leave_form.instance.st_leave_date, short_term_leave_form.instance.st_leave_finish_time)
            leave_check_difference_as_delta = start_time_date_leave_amount_check - finish_time_date_leave_amount_check
            leave_amount_requested = getLeaveAmount(leave_check_difference_as_delta)
            officers_leave_remaining = request.user.current_leave_total
            #Server side validation to ensure leave request is logical and that officer has enough leave remaining.
            if short_term_leave_form.instance.st_leave_start_time > short_term_leave_form.instance.st_leave_finish_time:
                messages.error(request, "The start time must be before the finish time.")
                return render(request, "submit_st_leave.html", {'short_term_leave_form': short_term_leave_form})
            elif leave_amount_requested > officers_leave_remaining:
                messages.error(request, "You do not have enough leave remaining to request this much leave.")
                return render(request, "submit_st_leave.html", {'short_term_leave_form': short_term_leave_form})
            else:
                st_leave_request = short_term_leave_form.save()
                start_time_date = datetime.datetime.combine(st_leave_request.st_leave_date, st_leave_request.st_leave_start_time)
                finish_time_date = datetime.datetime.combine(st_leave_request.st_leave_date, st_leave_request.st_leave_finish_time)
                difference_as_delta = finish_time_date - start_time_date
                #print(st_leave_request.st_leave_amount)
                st_leave_request.st_leave_amount = getLeaveAmount(difference_as_delta)
                st_leave_request.save() #ISSUE
                messages.success(request, 'You have successfully submitted a short term leave request.')
                return redirect(view_st_leave_request, st_leave_request.pk)
    else:
        short_term_leave_form = ShortTermAnnualLeaveRequestForm()
    return render(request, "submit_st_leave.html", {'short_term_leave_form': short_term_leave_form})
    
@login_required()
def view_st_leave_request(request, pk):
    '''
    This view retieve a specified short term leave request.
    '''
    st_leave_req = get_object_or_404(ShortTermAnnualLeaveRequest, pk=pk)
    applicants_leave_balance = st_leave_req.st_annual_leave_request_officer_id.current_leave_total
    #st_leave_req.save()
    return render(request, "view_st_leave_request.html", {'st_leave_req': st_leave_req, 'applicants_leave_balance': applicants_leave_balance})
    
@login_required()
def delete_short_term_leave_request(request, pk):
    '''
    This view along with conditional content on the view_st_leave_request.html template allows a user to delete a 
    short term leave request.
    '''
    st_leave_request_for_deletion = ShortTermAnnualLeaveRequest.objects.get(pk=pk)
    st_leave_request_for_deletion.delete()
    messages.success(request, "You have successfully deleted this short term leave request.")
    return redirect('annual_leave_page')
    
@login_required()
def edit_short_term_leave_request(request, pk):
    '''
    This view along with conditional content in the view_st_leave_request.html template allows a user to edit a 
    short term leave request prior to being checked by a validator.
    '''
    st_request_for_editing = get_object_or_404(ShortTermAnnualLeaveRequest, pk=pk) if pk else None
    if request.method == "POST":
        edit_st_request_form = ShortTermAnnualLeaveRequestForm(request.POST, request.FILES, instance=st_request_for_editing)
        if edit_st_request_form.is_valid():
            st_request_for_editing = edit_st_request_form.save()
            messages.success(request, 'You have successfully made changes to this short term leave request.')
            return redirect(view_st_leave_request, st_request_for_editing.pk)
    else:
        edit_st_request_form = ShortTermAnnualLeaveRequestForm(instance=st_request_for_editing)
    return render(request, "edit_st_request.html", {'st_request_for_editing': st_request_for_editing, 'edit_st_request_form': edit_st_request_form})
    
@login_required()
def view_my_leave_requests(request):
    '''
    This view returns two querysets. One for a user's annual leave requests and one for short term leave requests. 
    '''
    officer = request.user
    my_annual_leave_requests = AnnualLeaveRequest.objects.filter(al_request_officer_id=officer.pk)
    my_short_term_leave_requests = ShortTermAnnualLeaveRequest.objects.filter(st_annual_leave_request_officer_id=officer.pk)
    length_my_al_requests = len(my_annual_leave_requests)
    length_my_st_requests = len(my_short_term_leave_requests)
    
    return render(request, "my_leave_requests.html", {'my_annual_leave_requests': my_annual_leave_requests, 'my_short_term_leave_requests': my_short_term_leave_requests, 'length_my_al_requests': length_my_al_requests, 'length_my_st_requests': length_my_st_requests})

@login_required()
def view_staff_leave_submissions(request):
    '''
    This view collects all unchecked leave requests and presents them to a validator for checking.
    '''
    staff_submitted_al_requests = AnnualLeaveRequest.objects.select_related('al_request_officer_id').filter(leave_request_checked_by_validator=False)
    staff_submitted_st_requests = ShortTermAnnualLeaveRequest.objects.select_related('st_annual_leave_request_officer_id').filter(st_leave_request_checked_by_validator=False)
    
    #for i in staff_submitted_al_requests:
    #    print(i.al_request_officer_id.firstname)
    len_staff_submitted_al_requests = len(staff_submitted_al_requests)
    len_staff_submitted_st_requests = len(staff_submitted_st_requests)
    return render(request, "staff_leave_submissions.html", {'staff_submitted_al_requests': staff_submitted_al_requests, 'staff_submitted_st_requests': staff_submitted_st_requests, 'len_staff_submitted_al_requests': len_staff_submitted_al_requests, 'len_staff_submitted_st_requests': len_staff_submitted_st_requests})

@login_required()
def accept_block_leave(request, pk):
    '''
    This view allows a validator to accept an annual leave request. 
    It also calculates the total amount of leave taken and creates annual leave instances.
    '''
    leave_reg_being_accepted = AnnualLeaveRequest.objects.get(pk=pk)
    leave_start = leave_reg_being_accepted.leave_request_start_date
    leave_end = leave_reg_being_accepted.leave_request_last_date
    leave_hours_used = 0
    one_day_delta = datetime.timedelta(days=1)
    adjusted_end_date = leave_end + one_day_delta
    list_of_leave_dates = []
    
    for i in range((adjusted_end_date - leave_start).days):
        a_date = (leave_start + datetime.timedelta(days=i))
        list_of_leave_dates.append(a_date)
    
    for date in list_of_leave_dates:
        leave_date = Roster.objects.get(roster_shift_date=date, roster_officer_id=leave_reg_being_accepted.al_request_officer_id)
        if leave_date.roster_due_on == True:
            shift = Shift.objects.get(shift_label=leave_date.roster_shift_label)
            hours_used = shift.shift_duration
            leave_hours_used += hours_used
            #print(leave_hours_used)
            leave_record = AnnualLeave(al_officer_id=leave_reg_being_accepted.al_request_officer_id, al_date=date, leave_amount_used=hours_used)
            leave_record.save()
    
    leave_reg_being_accepted.leave_request_checked_by_validator = True
    leave_reg_being_accepted.leave_request_granted = True
    leave_reg_being_accepted.save()
    notify.send(request.user, recipient=leave_reg_being_accepted.al_request_officer_id, verb=" has granted your leave request: " + str(leave_reg_being_accepted))
    messages.success(request, 'You have granted this leave request.')
    
    leave_reg_being_accepted.al_request_officer_id.current_leave_total = leave_reg_being_accepted.al_request_officer_id.current_leave_total - leave_hours_used
    leave_reg_being_accepted.al_request_officer_id.save()
    
    return redirect('view_staff_leave_submissions')
    
@login_required()
def reject_annual_leave(request, pk):
    '''
    This view allows a validator to reject an annual leave request. It provides a form where the validator must provide a reason as 
    to why leave request being rejected.
    '''
    leave_being_rejected = AnnualLeaveRequest.objects.get(pk=pk)
    if request.method == 'POST':
        annual_leave_reject_form = AnnualLeaveRequestRejectForm(request.POST, request.FILES, instance=leave_being_rejected)
        if annual_leave_reject_form.is_valid():
            leave_being_rejected = annual_leave_reject_form.save()
            leave_being_rejected.leave_request_granted = False
            leave_being_rejected.leave_request_checked_by_validator = True
            leave_being_rejected.save()
            #NOTIFICATION TO APPLICANT THAT ANNUAL LEAVE REQUEST REJECTED.
            notify.send(request.user, recipient=leave_being_rejected.al_request_officer_id, verb=" has rejected your leave request: " + str(leave_being_rejected))
            messages.success(request, 'Leave Rejected.')
            return redirect('view_staff_leave_submissions')
    else:
        annual_leave_reject_form = AnnualLeaveRequestRejectForm(instance=leave_being_rejected)
    return render(request, "reject_al_request.html", {'leave_being_rejected': leave_being_rejected, 'annual_leave_reject_form': annual_leave_reject_form})
    