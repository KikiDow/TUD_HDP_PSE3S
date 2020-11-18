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