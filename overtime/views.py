from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import AllowancesRequest, NonScheduledOvertimeRequest, ShortOvertime, OvertimePerQtr, AvailabilitySheet, ShortTermAvailabilty, Overtime
from .forms import AllowancesRequestForm, NonScheduledOvertimeRequestForm, RejectAllowanceRequestForm, RejectNSOTForm, AvailabilitySheetForm, AssignOvertimeDateForm, AssignRecallStaffForm, AssignRequireStaffForm, ShortTermAvailabilityForm, AssignShortTermOTDateForm, AssignShortTermRecallStaffForm, AssignShortTermRequireStaffForm
import datetime as dt
from annual_leave.utils import getLeaveAmount
from .utils import getQtrDateIn, getNextQtr, getOfficerInstance
from notifications.signals import notify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from clocking.utils import convertStrToDateObj

# Create your views here.
@login_required()
def overtime_page(request):
    user = request.user
    users_overtime = Overtime.objects.filter(ot_officer_id=user)
    todays_date = dt.date.today()
    upcoming_overtime = []
    previous_overtime = []
    for ot in users_overtime:
        if ot.ot_date <= todays_date:
            previous_overtime.append(ot)
        else:
            upcoming_overtime.append(ot)
            
    length_upcoming_ot = len(upcoming_overtime)
    length_previous_ot = len(previous_overtime)
    
    upcoming_page = request.GET.get('upcoming_page', 1)
    upcoming_paginator = Paginator(upcoming_overtime, 8)
    try:
        upcoming_ot = upcoming_paginator.page(upcoming_page)
    except PageNotAnInteger:
        upcoming_ot = upcoming_paginator.page(1)
    except EmptyPage:
        upcoming_ot = upcoming_paginator.page(upcoming_paginator.num_pages)
        
    previous_page = request.GET.get('previous_page', 1)
    previous_paginator = Paginator(previous_overtime, 8)
    try:
        previous_ot = previous_paginator.page(previous_page)
    except PageNotAnInteger:
        previous_ot = previous_paginator.page(1)
    except EmptyPage:
        previous_ot = previous_paginator.page(previous_paginator.num_pages)
        
    return render(request, "overtime_page.html", {'upcoming_ot': upcoming_ot, 'previous_ot': previous_ot, 'length_upcoming_ot': length_upcoming_ot, 'length_previous_ot': length_previous_ot})

@login_required()
def search_previous_ot(request):
    user = request.user
    previous_ot_search_date = request.GET['q']
    date = convertStrToDateObj(previous_ot_search_date)
    previous_ot_search_result = Overtime.objects.filter(ot_officer_id=user, ot_date=date)
    
    page = request.GET.get('page', 1)
    
    paginator = Paginator(previous_ot_search_result, 8)
    try:
        previous_ot = paginator.page(page)
    except PageNotAnInteger:
        previous_ot = paginator.page(1)
    except EmptyPage:
        previous_ot = paginator.page(paginator.num_pages)
    
    return render(request, "previous_ot_search.html", {'previous_ot': previous_ot})

@login_required()
def allowances_page(request):
    user = request.user
    user_allowance_requests = AllowancesRequest.objects.filter(allow_req_off_id=user).order_by('-allow_req_date')
    len_allowance_requests = len(user_allowance_requests)
    page = request.GET.get('page', 1)
    
    paginator = Paginator(user_allowance_requests, 8)
    try:
        allowance_requests = paginator.page(page)
    except PageNotAnInteger:
        allowance_requests = paginator.page(1)
    except EmptyPage:
        allowance_requests = paginator.page(paginator.num_pages)
    
    return render(request, "allowances_page.html", {'allowance_requests': allowance_requests, 'len_allowance_requests': len_allowance_requests})
    
@login_required()
def search_allowances(request):
    user = request.user
    allowance_search_date = request.GET['q']
    date = convertStrToDateObj(allowance_search_date)
    allowance_search_result = AllowancesRequest.objects.filter(allow_req_off_id=user, allow_req_date=date)
   
    page = request.GET.get('page', 1)
    
    paginator = Paginator(allowance_search_result, 8)
    try:
        allowance_requests = paginator.page(page)
    except PageNotAnInteger:
        allowance_requests = paginator.page(1)
    except EmptyPage:
        allowance_requests = paginator.page(paginator.num_pages)
    
    return render(request, "allowance_search.html", {'allowance_requests': allowance_requests})
    
    
@login_required()
def submit_allowance_request(request):
    if request.method == "POST":
        allowance_req_form = AllowancesRequestForm(request.POST, request.FILES)
        if allowance_req_form.is_valid():
            allowance_req_form.instance.allow_req_off_id = request.user
            #Check that user is not accidentally submitting allowance requests in advance.
            todays_date = dt.date.today()
            if allowance_req_form.instance.allow_req_date > todays_date:
                messages.error(request, "You cannot submit allowance requests in advance of todays date.")
                return render(request, "submit_allowance_request.html", {'allowance_req_form': allowance_req_form})
            #Check that the user has selected at least one allowance in their claim.
            if allowance_req_form.instance.claiming_breakfast_allowance == False and allowance_req_form.instance.claiming_dinner_allowance == False and allowance_req_form.instance.claiming_tea_allowance == False and allowance_req_form.instance.claiming_plain_clothes_allowance == False and allowance_req_form.instance.claiming_food_for_prisoner_expense == False:
                messages.error(request, "You must select at least one allowance to make a valid allowance request.")
                return render(request, "submit_allowance_request.html", {'allowance_req_form': allowance_req_form})
            if allowance_req_form.instance.claiming_food_for_prisoner_expense == True:
                if allowance_req_form.instance.food_for_prisoner_amount is None:
                    messages.error(request, "You must include the cost of the prisoner's meal to claim this expense.")
                    return render(request, "submit_allowance_request.html", {'allowance_req_form': allowance_req_form})
                elif allowance_req_form.instance.receipt_for_prisoner_food is False:
                    messages.error(request, "You must provide a photograph of the receipt for the prisoner's meal to claim this expense.")
                    return render(request, "submit_allowance_request.html", {'allowance_req_form': allowance_req_form})
                else:
                    allowance_request = allowance_req_form.save()
                    total_claim_amount = 0.0
                    if allowance_request.claiming_breakfast_allowance == True:
                        total_claim_amount += settings.BREAKFAST_ALLOWANCE
                    if allowance_request.claiming_dinner_allowance == True:
                        total_claim_amount += settings.DINNER_ALLOWANCE
                    if allowance_request.claiming_tea_allowance == True:
                        total_claim_amount += settings.TEA_ALLOWANCE
                    if allowance_request.claiming_plain_clothes_allowance == True:
                        total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE
                    if allowance_request.claiming_food_for_prisoner_expense == True:
                        total_claim_amount += allowance_request.food_for_prisoner_amount
                    allowance_request.claim_total = total_claim_amount
                    allowance_request.save()
                    return redirect(view_allowance_request, allowance_request.pk)
            else:
                allowance_request = allowance_req_form.save()
                total_claim_amount = 0.0
                if allowance_request.claiming_breakfast_allowance == True:
                    total_claim_amount += settings.BREAKFAST_ALLOWANCE
                if allowance_request.claiming_dinner_allowance == True:
                    total_claim_amount += settings.DINNER_ALLOWANCE
                if allowance_request.claiming_tea_allowance == True:
                    total_claim_amount += settings.TEA_ALLOWANCE
                if allowance_request.claiming_plain_clothes_allowance == True:
                    total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE
                if allowance_request.claiming_food_for_prisoner_expense == True:
                    total_claim_amount += allowance_request.food_for_prisoner_amount
                allowance_request.claim_total = total_claim_amount
                allowance_request.save()
                return redirect(view_allowance_request, allowance_request.pk)
    else:
        allowance_req_form = AllowancesRequestForm()
    return render(request, "submit_allowance_request.html", {'allowance_req_form': allowance_req_form})
    
@login_required()    
def view_allowance_request(request, pk):
    allow_req_to_view = get_object_or_404(AllowancesRequest, pk=pk)
    allow_req_to_view.save()
    return render(request, "view_allowance_request.html", {'allow_req_to_view': allow_req_to_view})
    
@login_required()
def edit_allowance_request(request, pk):
    allow_req_for_editing = get_object_or_404(AllowancesRequest, pk=pk) if pk else None
    if request.method == "POST":
        edit_allow_req_form = AllowancesRequestForm(request.POST, request.FILES, instance=allow_req_for_editing)
        if edit_allow_req_form.is_valid():
            #Check that user is not accidentally submitting allowance requests in advance.
            todays_date = dt.date.today()
            if edit_allow_req_form.instance.allow_req_date > todays_date:
                messages.error(request, "You cannot submit allowance requests in advance of todays date.")
                return render(request, "edit_allowance_request.html", {'edit_allow_req_form': edit_allow_req_form})
            #Check that the user has selected at least one allowance in their claim.
            if edit_allow_req_form.instance.claiming_breakfast_allowance == False and edit_allow_req_form.instance.claiming_dinner_allowance == False and edit_allow_req_form.instance.claiming_tea_allowance == False and edit_allow_req_form.instance.claiming_plain_clothes_allowance == False and edit_allow_req_form.instance.claiming_food_for_prisoner_expense == False:
                messages.error(request, "You must select at least one allowance to make a valid allowance request.")
                return render(request, "edit_allowance_request.html", {'edit_allow_req_form': edit_allow_req_form})
            if edit_allow_req_form.instance.claiming_food_for_prisoner_expense == True:
                if edit_allow_req_form.instance.food_for_prisoner_amount is None:
                    messages.error(request, "You must include the cost of the prisoner's meal to claim this expense.")
                    return render(request, "edit_allowance_request.html", {'edit_allow_req_form': edit_allow_req_form})
                elif edit_allow_req_form.instance.receipt_for_prisoner_food is False:
                    messages.error(request, "You must provide a photograph of the receipt for the prisoner's meal to claim this expense.")
                    return render(request, "edit_allowance_request.html", {'edit_allow_req_form': edit_allow_req_form})
                else:
                    allow_req_for_editing = edit_allow_req_form.save()
                    total_claim_amount = 0.0
                    if allow_req_for_editing.claiming_breakfast_allowance == True:
                        total_claim_amount += settings.BREAKFAST_ALLOWANCE
                    if allow_req_for_editing.claiming_dinner_allowance == True:
                        total_claim_amount += settings.DINNER_ALLOWANCE
                    if allow_req_for_editing.claiming_tea_allowance == True:
                        total_claim_amount += settings.TEA_ALLOWANCE
                    if allow_req_for_editing.claiming_plain_clothes_allowance == True:
                        total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE
                    if allow_req_for_editing.claiming_food_for_prisoner_expense == True:
                        total_claim_amount += allow_req_for_editing.food_for_prisoner_amount
                    allow_req_for_editing.claim_total = total_claim_amount
                    allow_req_for_editing.save()
                    return redirect(view_allowance_request, allow_req_for_editing.pk)
            else:
                allow_req_for_editing = edit_allow_req_form.save()
                total_claim_amount = 0.0
                if allow_req_for_editing.claiming_breakfast_allowance == True:
                    total_claim_amount += settings.BREAKFAST_ALLOWANCE
                if allow_req_for_editing.claiming_dinner_allowance == True:
                    total_claim_amount += settings.DINNER_ALLOWANCE
                if allow_req_for_editing.claiming_tea_allowance == True:
                    total_claim_amount += settings.TEA_ALLOWANCE
                if allow_req_for_editing.claiming_plain_clothes_allowance == True:
                    total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE
                if allow_req_for_editing.claiming_food_for_prisoner_expense == True:
                    total_claim_amount += allow_req_for_editing.food_for_prisoner_amount                    
                allow_req_for_editing.claim_total = total_claim_amount
                allow_req_for_editing.save()
                return redirect(view_allowance_request, allow_req_for_editing.pk)
    else:
        edit_allow_req_form = AllowancesRequestForm(instance=allow_req_for_editing)
    return render(request, "edit_allowance_request.html", {'allow_req_for_editing': allow_req_for_editing, 'edit_allow_req_form': edit_allow_req_form})
    
@login_required()
def delete_allowance_request(request, pk):
    allowance_req_for_deletion = AllowancesRequest.objects.get(pk=pk)
    allowance_req_for_deletion.delete()
    messages.success(request, "You have successfully deleted this allowance request.")
    return redirect(allowances_page)
    
@login_required()
def view_staff_allowance_requests(request):
    user = request.user
    staff_allowance_requests = AllowancesRequest.objects.filter(allow_req_checked_by_validator=False).exclude(allow_req_off_id=user.pk)
    length_of_staff_allow_req = len(staff_allowance_requests)
    return render(request, "view_staff_allowance_requests.html", {'staff_allowance_requests': staff_allowance_requests, 'length_of_staff_allow_req': length_of_staff_allow_req})
    
@login_required()
def accept_allowance_request(request, pk):
    allow_req_being_accepted = AllowancesRequest.objects.get(pk=pk)
    allow_req_being_accepted.allow_req_checked_by_validator = True
    allow_req_being_accepted.allow_req_accepted = True
    allow_req_being_accepted.save()
    #NOTIFICATION TO APPLCANT THAT ALLOWANCE REQUEST HAS BEEN ACCEPTED.
    notify.send(request.user, recipient=allow_req_being_accepted.allow_req_off_id, verb=" has accepted your allowance request : " + str(allow_req_being_accepted.allow_req_date))
    messages.success(request, "You have accepted this allowance request.")
    return redirect('view_staff_allowance_requests')
    
@login_required()
def reject_allowance_request(request, pk):
    allow_req_being_rejected = AllowancesRequest.objects.get(pk=pk)
    if request.method == "POST":
        allow_req_reject_form = RejectAllowanceRequestForm(request.POST, request.FILES, instance=allow_req_being_rejected)
        if allow_req_reject_form.is_valid():
            allow_req_being_rejected = allow_req_reject_form.save()
            allow_req_being_rejected.allow_req_checked_by_validator = True
            allow_req_being_rejected.allow_req_accepted = False
            allow_req_being_rejected.save()
            #NOTIFICATION TO APPLCANT THAT ALLOWANCE REQUEST HAS BEEN REJECTED.
            notify.send(request.user, recipient=allow_req_being_rejected.allow_req_off_id, verb=" has rejected your allowance request : " + str(allow_req_being_rejected.allow_req_date))
            messages.success(request, "You have rejected this allowance request.")
    else:
        allow_req_reject_form = RejectAllowanceRequestForm(instance=allow_req_being_rejected)
    return render(request, "reject_allow_request.html", {'allow_req_being_rejected': allow_req_being_rejected, 'allow_req_reject_form': allow_req_reject_form})
    
@login_required()
def non_scheduled_ot_page(request):
    user = request.user
    user_non_scheduled_ot_requests = NonScheduledOvertimeRequest.objects.filter(nsot_off_id=user).order_by('-nsot_date')
    len_my_non_scheduled_ot_requests = len(user_non_scheduled_ot_requests)
    
    page = request.GET.get('page', 1)
    
    paginator = Paginator(user_non_scheduled_ot_requests, 8)
    try:
        my_non_scheduled_ot_requests = paginator.page(page)
    except PageNotAnInteger:
        my_non_scheduled_ot_requests = paginator.page(1)
    except EmptyPage:
        my_non_scheduled_ot_requests = paginator.page(paginator.num_pages)
        
    return render(request, "nsot_page.html", {'my_non_scheduled_ot_requests': my_non_scheduled_ot_requests, 'len_my_non_scheduled_ot_requests': len_my_non_scheduled_ot_requests})
    
@login_required()
def search_nsot(request):
    user = request.user
    nsot_search_date = request.GET['q']
    date = convertStrToDateObj(nsot_search_date)
    nsot_search_result = NonScheduledOvertimeRequest.objects.filter(nsot_off_id=user, nsot_date=date)
   
    page = request.GET.get('page', 1)
    
    paginator = Paginator(nsot_search_result, 8)
    try:
        my_non_scheduled_ot_requests = paginator.page(page)
    except PageNotAnInteger:
        my_non_scheduled_ot_requests = paginator.page(1)
    except EmptyPage:
        my_non_scheduled_ot_requests = paginator.page(paginator.num_pages)
    
    return render(request, "nsot_search.html", {'my_non_scheduled_ot_requests': my_non_scheduled_ot_requests})
    
@login_required()
def submit_nsot_request(request):
    if request.method == "POST":
        nsot_req_form = NonScheduledOvertimeRequestForm(request.POST, request.FILES)
        if nsot_req_form.is_valid():
            nsot_req_form.instance.nsot_off_id = request.user
            #Check that user is not accidentally submitting nsot requests in advance.
            todays_date = dt.date.today()
            if nsot_req_form.instance.nsot_date > todays_date:
                messages.error(request, "You cannot submit Non-Scheduled Overtime requests in advance of todays date.")
                return render(request, "submit_nsot_request.html", {'nsot_req_form': nsot_req_form})
            #Check that the end_time is not before the start_time.
            if nsot_req_form.instance.nsot_start_time > nsot_req_form.instance.nsot_end_time:
                messages.error(request, "The start time must be before the finish time.")
                return render(request, "submit_nsot_request.html", {'nsot_req_form': nsot_req_form})
            else:
                nsot_request = nsot_req_form.save()
                date_time_start = dt.datetime.combine(nsot_request.nsot_date, nsot_request.nsot_start_time)
                date_time_end = dt.datetime.combine(nsot_request.nsot_date, nsot_request.nsot_end_time)
                nsot_difference_as_delta = date_time_end - date_time_start
                nsot_request.ot_hours_claimed = getLeaveAmount(nsot_difference_as_delta)
                nsot_request.save()
                messages.success(request, "Non Scheduled Overtime Request successfully submitted.")
                return redirect(view_non_scheduled_overtime_request, nsot_request.id)
    else:
        nsot_req_form = NonScheduledOvertimeRequestForm()
    return render(request, "submit_nsot_request.html", {'nsot_req_form': nsot_req_form})
    
@login_required()
def view_non_scheduled_overtime_request(request, pk):
    nsot_req_to_view = get_object_or_404(NonScheduledOvertimeRequest, pk=pk)
    nsot_req_to_view.save()
    return render(request, "view_nsot_request.html", {'nsot_req_to_view': nsot_req_to_view})
    
@login_required()
def delete_nsot_request(request, pk):
    nsot_req_for_deletion = NonScheduledOvertimeRequest.objects.get(pk=pk)
    nsot_req_for_deletion.delete()
    messages.success(request, "You have successfully deleted this non-scheduled overtime request.")
    return redirect(non_scheduled_ot_page)
    
@login_required()
def edit_nsot_request(request, pk):
    nsot_req_for_editing = get_object_or_404(NonScheduledOvertimeRequest, pk=pk) if pk else None
    if request.method == "POST":
        edit_nsot_form = NonScheduledOvertimeRequestForm(request.POST, request.FILES, instance=nsot_req_for_editing)
        if edit_nsot_form.is_valid():
            #Check that user is not attempting to edit nsot requests for advance dates.
            todays_date = dt.date.today()
            if edit_nsot_form.instance.nsot_date > todays_date:
                messages.error(request, "You cannot submit Non-Scheduled Overtime requests in advance of todays date.")
                return render(request, "edit_nsot_request.html", {'edit_nsot_form': edit_nsot_form})
            #Check that user has not edited the end time to be before the start time.
            if edit_nsot_form.instance.nsot_start_time > edit_nsot_form.instance.nsot_end_time:
                messages.error(request, "The start date for the non scheduled overtime request must be before the end date.")
                return render(request, "edit_nsot_request.html", {'edit_nsot_form': edit_nsot_form})
            else:
                nsot_req_for_editing = edit_nsot_form.save()
                #Combine date and time data to create datetime objects so that they can be used to calculate ot_hours_claimed.
                date_time_start = dt.datetime.combine(nsot_req_for_editing.nsot_date, nsot_req_for_editing.nsot_start_time)
                date_time_end = dt.datetime.combine(nsot_req_for_editing.nsot_date, nsot_req_for_editing.nsot_end_time)
                #Calculate the amount of leave being requested.
                nsot_difference_as_delta = date_time_end - date_time_start
                nsot_req_for_editing.ot_hours_claimed = getLeaveAmount(nsot_difference_as_delta)
                nsot_req_for_editing.save()
                messages.success(request, 'You have successfully made changes to this non scheduled overtime request.')
                return redirect(view_non_scheduled_overtime_request, nsot_req_for_editing.pk)
    else:
        edit_nsot_form = NonScheduledOvertimeRequestForm(instance=nsot_req_for_editing)
    return render(request, "edit_nsot_request.html", {'nsot_req_for_editing': nsot_req_for_editing, 'edit_nsot_form': edit_nsot_form})
    
@login_required()
def view_staff_nsot_requests(request):
    user = request.user
    staff_nsot_requests = NonScheduledOvertimeRequest.objects.filter(nsot_checked_by_validator=False).exclude(nsot_off_id=user.pk)
    length_of_staff_nsot_req = len(staff_nsot_requests)
    return render(request, "view_staff_nsot_requests.html", {'staff_nsot_requests': staff_nsot_requests, 'length_of_staff_nsot_req': length_of_staff_nsot_req})
    
@login_required()
def accept_nsot_request(request, pk):
    nsot_req_being_accepted = NonScheduledOvertimeRequest.objects.get(pk=pk)
    nsot_req_being_accepted.nsot_checked_by_validator = True
    nsot_req_being_accepted.nsot_accepted = True
    nsot_req_being_accepted.save()
    qtr_application_date_in = getQtrDateIn(nsot_req_being_accepted.nsot_date)
    new_short_overtime_record = ShortOvertime(short_ot_officer_id=nsot_req_being_accepted.nsot_off_id, short_ot_qtr_id=qtr_application_date_in.id, short_ot_date=nsot_req_being_accepted.nsot_date, short_ot_start_time=nsot_req_being_accepted.nsot_start_time, short_ot_end_time=nsot_req_being_accepted.nsot_end_time, overtime_hours=nsot_req_being_accepted.ot_hours_claimed)
    new_short_overtime_record.save()
    officers_ot_per_qtr = OvertimePerQtr.objects.get(ot_per_qtr_off_id=nsot_req_being_accepted.nsot_off_id, ot_per_qtr_qtr_id=qtr_application_date_in.id)
    officers_ot_per_qtr.ot_hours_completed += nsot_req_being_accepted.ot_hours_claimed
    officers_ot_per_qtr.save()
    #NOTIFICATION TO APPLICANT THAT NSOT REQUEST HAS BEEN ACCEPTED.
    notify.send(request.user, recipient=nsot_req_being_accepted.nsot_off_id, verb=" has accepted your non-scheduled overtime request : " + str(nsot_req_being_accepted.nsot_date))
    messages.success(request, "You have accepted this non scheduled overtime request.")
    return redirect('view_staff_nsot_requests')
    
@login_required()
def reject_nsot_request(request, pk):
    nsot_req_being_rejected = NonScheduledOvertimeRequest.objects.get(pk=pk)
    if request.method == "POST":
        nsot_req_reject_form = RejectNSOTForm(request.POST, request.FILES, instance=nsot_req_being_rejected)
        if nsot_req_reject_form.is_valid():
            nsot_req_being_rejected = nsot_req_reject_form.save()
            nsot_req_being_rejected.nsot_req_checked_by_validator = True
            nsot_req_being_rejected.nsot_req_accepted = False
            nsot_req_being_rejected.save()
            #NOTIFICATION TO APPLCANT THAT NSOT REQUEST HAS BEEN REJECTED.
            notify.send(request.user, recipient=nsot_req_being_rejected.nsot_off_id, verb=" has rejected your non-scheduled overtime request : " + str(nsot_req_being_rejected.nsot_date))
            messages.success(request, "You have rejected this non scheduled overtime request.")
    else:
        nsot_req_reject_form = RejectNSOTForm(instance=nsot_req_being_rejected)
    return render(request, "reject_nsot_request.html", {'nsot_req_being_rejected': nsot_req_being_rejected, 'nsot_req_reject_form': nsot_req_reject_form})
    
@login_required()
def availability_page(request):
    user = request.user
    my_availability_sheets = AvailabilitySheet.objects.filter(avail_sheet_off_id=user.pk)
    len_my_availability_sheets = len(my_availability_sheets)
    my_short_term_availability = ShortTermAvailabilty.objects.filter(st_availability_off_id=user.pk)
    len_my_st_availability = len(my_short_term_availability)
    
    return render(request, "availability_page.html", {'my_availability_sheets': my_availability_sheets, 'my_short_term_availability': my_short_term_availability, 'len_my_availability_sheets': len_my_availability_sheets, 'len_my_st_availability': len_my_st_availability})
    
@login_required()
def submit_availability_sheet(request):
    if request.method == "POST":
        availability_sheet_form = AvailabilitySheetForm(request.POST, request.FILES)
        mon_one = request.POST.get('mon_one')
        availability_sheet_form.fields['mon_one'].choices = [(mon_one, mon_one)]
        mon_two = request.POST.get('mon_two')
        availability_sheet_form.fields['mon_two'].choices = [(mon_two, mon_two)]
        tue_one = request.POST.get('tue_one')
        availability_sheet_form.fields['tue_one'].choices = [(tue_one, tue_one)]
        tue_two = request.POST.get('tue_two')
        availability_sheet_form.fields['tue_two'].choices = [(tue_two, tue_two)]
        wed_one = request.POST.get('wed_one')
        availability_sheet_form.fields['wed_one'].choices = [(wed_one, wed_one)]
        wed_two = request.POST.get('wed_two')
        availability_sheet_form.fields['wed_two'].choices = [(wed_two, wed_two)]
        thurs_one = request.POST.get('thurs_one')
        availability_sheet_form.fields['thurs_one'].choices = [(thurs_one, thurs_one)]
        thurs_two = request.POST.get('thurs_two')
        availability_sheet_form.fields['thurs_two'].choices = [(thurs_two, thurs_two)]
        fri_one = request.POST.get('fri_one')
        availability_sheet_form.fields['fri_one'].choices = [(fri_one, fri_one)]
        fri_two = request.POST.get('fri_two')
        availability_sheet_form.fields['fri_two'].choices = [(fri_two, fri_two)]
        sat_one = request.POST.get('sat_one')
        availability_sheet_form.fields['sat_one'].choices = [(sat_one, sat_one)]
        sat_two = request.POST.get('sat_two')
        availability_sheet_form.fields['sat_two'].choices = [(sat_two, sat_two)]
        sun_one = request.POST.get('sun_one')
        availability_sheet_form.fields['sun_one'].choices = [(sun_one, sun_one)]
        sun_two = request.POST.get('sun_two')
        availability_sheet_form.fields['sun_two'].choices = [(sun_two, sun_two)]
        
        if availability_sheet_form.is_valid():
            availability_sheet_form.instance.avail_sheet_off_id = request.user
            availability_sheet_form.instance.avail_sheet_qtr_id = getNextQtr()
            if availability_sheet_form.instance.mon_one == availability_sheet_form.instance.mon_two:
                messages.error(request, "The two mondays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            elif availability_sheet_form.instance.tue_one == availability_sheet_form.instance.tue_two:
                messages.error(request, "The two tuesdays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            elif availability_sheet_form.instance.wed_one == availability_sheet_form.instance.wed_two:
                messages.error(request, "The two wednesdays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            elif availability_sheet_form.instance.thurs_one == availability_sheet_form.instance.thurs_two:
                messages.error(request, "The two thursdays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            elif availability_sheet_form.instance.fri_one == availability_sheet_form.instance.fri_two:
                messages.error(request, "The two fridays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            elif availability_sheet_form.instance.sat_one == availability_sheet_form.instance.sat_two:
                messages.error(request, "The two saturdays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            elif availability_sheet_form.instance.sun_one == availability_sheet_form.instance.sun_two:
                messages.error(request, "The two wednesdays you have selected are the same date.")
                return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
            else:
                availability_sheet = availability_sheet_form.save()
                messages.success(request, "Availability Sheet successfully submitted.")
                return redirect(view_availability_sheet, availability_sheet.id)
    else:
        availability_sheet_form = AvailabilitySheetForm()
    return render(request, "submit_availability_sheet.html", {'availability_sheet_form': availability_sheet_form})
    
@login_required()
def view_availability_sheet(request, pk):
    avail_sheet_to_view = get_object_or_404(AvailabilitySheet, pk=pk)
    avail_sheet_to_view.save()
    return render(request, "view_availability_sheet.html", {'avail_sheet_to_view': avail_sheet_to_view})
    
@login_required()
def delete_availability_sheet(request, pk):
    avail_sheet_for_deletion = AvailabilitySheet.objects.get(pk=pk)
    avail_sheet_for_deletion.delete()
    messages.success(request, "You have successfully deleted this availability sheet.")
    return redirect(availability_page)
    
@login_required()
def assign_ot_date(request):
    if request.method == "POST":
        assign_ot_date_form = AssignOvertimeDateForm(request.POST, request.FILES)
        if assign_ot_date_form.is_valid():
            chosen_date = assign_ot_date_form.cleaned_data.get("date_for_assignment")
            #print("Inside ot date view: " + str(chosen_date))
            return redirect(assign_ot_recall, chosen_date)
    else:
        assign_ot_date_form = AssignOvertimeDateForm()
    return render(request, "assign_ot_date.html", {'assign_ot_date_form': assign_ot_date_form})
    
@login_required()
def assign_ot_recall(request, chosen_date):
    date_selected = chosen_date
    if request.method == "POST":
        assign_recall_form = AssignRecallStaffForm(request.POST, request.FILES, initial={'selected_date': date_selected})
        officers_available = request.POST.get('officers_available')
        assign_recall_form.fields['officers_available'].choices = [(officers_available, officers_available)]
        if assign_recall_form.is_valid():
            officer = assign_recall_form.cleaned_data.get("officers_available")
            officer_instance = getOfficerInstance(officer)
            date = assign_recall_form.cleaned_data.get("selected_date")
            quarter = getQtrDateIn(date)
            shift = assign_recall_form.cleaned_data.get("assign_shift")
            new_overtime = Overtime(ot_officer_id=officer_instance, ot_qtr_id=quarter, ot_date=date, ot_shift_id=shift, ot_recall=True)
            new_overtime.save()
            notify.send(request.user, recipient=new_overtime.ot_officer_id, verb=" has required you for overtime on : " + str(new_overtime.ot_date))
            messages.success(request, "Staff successfully recalled.")
            return redirect(overtime_page)
    else:
        assign_recall_form = AssignRecallStaffForm(initial = {'selected_date': date_selected})
    return render(request, "assign_ot_recall.html", {'assign_recall_form': assign_recall_form, 'date_selected': date_selected})
    
@login_required()
def assign_ot_require(request, date_selected):
    date_for_require = date_selected
    if request.method == "POST":
        assign_require_form = AssignRequireStaffForm(request.POST, request.FILES, initial = {'selected_require_date': date_for_require})
        officers_for_require = request.POST.get('officers_for_require')
        assign_require_form.fields['officers_for_require'].choices = [(officers_for_require, officers_for_require)]
        if assign_require_form.is_valid():
            officer = assign_require_form.cleaned_data.get("officers_for_require")
            officer_instance = getOfficerInstance(officer)
            date = assign_require_form.cleaned_data.get("selected_require_date")
            quarter = getQtrDateIn(date)
            shift = assign_require_form.cleaned_data.get("assign_require_shift")
            new_overtime = Overtime(ot_officer_id=officer_instance, ot_qtr_id=quarter, ot_date=date, ot_shift_id=shift, ot_requirement=True)
            new_overtime.save()
            notify.send(request.user, recipient=new_overtime.ot_officer_id, verb=" has required you for overtime on : " + str(new_overtime.ot_date))
            messages.success(request, "Staff successfully required.")
            return redirect(overtime_page)
    else:
        assign_require_form = AssignRequireStaffForm(initial = {'selected_require_date': date_for_require})
    return render(request, "assign_ot_require.html", {'assign_require_form': assign_require_form})
    
@login_required()
def submit_st_availability(request):
    if request.method == "POST":
        short_term_availability_form = ShortTermAvailabilityForm(request.POST, request.FILES)
        st_availability_date = request.POST.get('st_availability_date')
        short_term_availability_form.fields['st_availability_date'].choices = [(st_availability_date, st_availability_date)]
        if short_term_availability_form.is_valid():
            short_term_availability_form.instance.st_availability_off_id = request.user
            short_term_availability_form.instance.st_availability_qtr_id = getQtrDateIn(short_term_availability_form.instance.st_availability_date)
            short_term_availability_submission = short_term_availability_form.save()
            messages.success(request, "Short Term Availability successfully submitted.")
            return redirect(availability_page)
    else:
        short_term_availability_form = ShortTermAvailabilityForm()
    return render(request, "submit_st_availability_submission.html", {'short_term_availability_form': short_term_availability_form})
    
@login_required()
def delete_st_availability_submission(request, pk):
    st_avail_submission_for_deletion = ShortTermAvailabilty.objects.get(pk=pk)
    st_avail_submission_for_deletion.delete()
    messages.success(request, "You have successfully deleted this short-term availability submission.")
    return redirect(availability_page)
    
@login_required()
def assign_st_ot_date(request):
    if request.method == "POST":
        assign_st_ot_date_form = AssignShortTermOTDateForm(request.POST, request.FILES)
        if assign_st_ot_date_form.is_valid():
            todays_date = dt.date.today()
            one_day_delta = dt.timedelta(days=1)
            st_window_start = todays_date + one_day_delta
            thirteen_day_delta = dt.timedelta(days=13)
            short_term_window_end = todays_date + thirteen_day_delta
            chosen_st_date = assign_st_ot_date_form.cleaned_data.get("date_for_st_assignment")
            if chosen_st_date < st_window_start or chosen_st_date > short_term_window_end:
                messages.error(request, "The date you have selected is not within the short term recall window.")
                return render(request, "assign_st_ot_date.html", {'assign_st_ot_date_form': assign_st_ot_date_form})
            else:
                return redirect(assign_st_ot_recall, chosen_st_date)
    else:
        assign_st_ot_date_form = AssignShortTermOTDateForm()
    return render(request, "assign_st_ot_date.html", {'assign_st_ot_date_form': assign_st_ot_date_form})
    
@login_required()
def assign_st_ot_recall(request, chosen_st_date):
    st_date_selected = chosen_st_date
    if request.method == "POST":
        assign_st_recall_form = AssignShortTermRecallStaffForm(request.POST, request.FILES, initial={'selected_st_date': st_date_selected})
        officers_available = request.POST.get('officers_available')
        #len_available_officers = available_officers.count()
        assign_st_recall_form.fields['officers_available'].choices = [(officers_available, officers_available)]
        if assign_st_recall_form.is_valid():
            officer = assign_st_recall_form.cleaned_data.get("officers_available")
            officer_instance = getOfficerInstance(officer)
            date = assign_st_recall_form.cleaned_data.get("selected_st_date")
            quarter = getQtrDateIn(date)
            shift = assign_st_recall_form.cleaned_data.get("assign_shift")
            new_overtime = Overtime(ot_officer_id=officer_instance, ot_qtr_id=quarter, ot_date=date, ot_shift_id=shift, ot_recall=True)
            new_overtime.save()
            #NOTIFICATION TO STAFF MEMBER OF SHORT TERM RECALL
            messages.success(request, "Staff successfully recalled in the short-term.")
            return redirect(overtime_page)
    else:
        assign_st_recall_form = AssignShortTermRecallStaffForm(initial = {'selected_st_date': st_date_selected})
    return render(request, "assign_st_ot_recall.html", {'assign_st_recall_form': assign_st_recall_form, 'st_date_selected': st_date_selected})
    
@login_required()
def assign_st_ot_require(request, st_date_selected):
    date_for_st_require = st_date_selected
    #print(date_for_require)
    if request.method == "POST":
        assign_st_require_form = AssignShortTermRequireStaffForm(request.POST, request.FILES, initial = {'selected_st_require_date': date_for_st_require})
        officers_for_require = request.POST.get('officers_for_require')
        assign_st_require_form.fields['officers_for_require'].choices = [(officers_for_require, officers_for_require)]
        if assign_st_require_form.is_valid():
            officer = assign_st_require_form.cleaned_data.get("officers_for_require")
            officer_instance = getOfficerInstance(officer)
            date = assign_st_require_form.cleaned_data.get("selected_st_require_date")
            quarter = getQtrDateIn(date)
            shift = assign_st_require_form.cleaned_data.get("assign_require_shift")
            new_overtime = Overtime(ot_officer_id=officer_instance, ot_qtr_id=quarter, ot_date=date, ot_shift_id=shift, ot_requirement=True)
            new_overtime.save()
            #Notification that staff member has been required.
            messages.success(request, "Staff successfully required in the short-term.")
            return redirect(overtime_page)
    else:
        assign_st_require_form = AssignShortTermRequireStaffForm(initial = {'selected_st_require_date': date_for_st_require})
    return render(request, "assign_st_ot_require.html", {'assign_st_require_form': assign_st_require_form})