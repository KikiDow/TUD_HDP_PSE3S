from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import AllowancesRequest, NonScheduledOvertimeRequest, ShortOvertime, OvertimePerQtr, AvailabilitySheet, ShortTermAvailabilty, Overtime
from .forms import AllowancesRequestForm, NonScheduledOvertimeRequestForm, RejectAllowanceRequestForm, RejectNSOTForm, AvailabilitySheetForm, AssignOvertimeDateForm, AssignRecallStaffForm, AssignRequireStaffForm
import datetime
from annual_leave.utils import getLeaveAmount
from .utils import getQtrDateIn, getNextQtr

# Create your views here.
@login_required()
def overtime_page(request):
    return render(request, "overtime_page.html")
    
@login_required()
def allowances_page(request):
    user = request.user
    allowance_requests = AllowancesRequest.objects.filter(allow_req_off_id=user.pk)
    len_allowance_requests = len(allowance_requests)
    return render(request, "allowances_page.html", {'allowance_requests': allowance_requests, 'len_allowance_requests': len_allowance_requests})