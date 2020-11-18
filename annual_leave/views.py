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
