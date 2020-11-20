from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import AllowancesRequest, NonScheduledOvertimeRequest, ShortOvertime, OvertimePerQtr, AvailabilitySheet, ShortTermAvailabilty, Overtime
from .forms import AllowancesRequestForm, NonScheduledOvertimeRequestForm, RejectAllowanceRequestForm, RejectNSOTForm, AvailabilitySheetForm, AssignOvertimeDateForm, AssignRecallStaffForm, AssignRequireStaffForm
import datetime
from annual_leave.utils import getLeaveAmount
from .utils import getQtrDateIn, getNextQtr
from notifications.signals import notify

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
    
@login_required()
def submit_allowance_request(request):
    if request.method == "POST":
        allowance_req_form = AllowancesRequestForm(request.POST, request.FILES)
        if allowance_req_form.is_valid():
            allowance_req_form.instance.allow_req_off_id = request.user
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
    my_non_scheduled_ot_requests = NonScheduledOvertimeRequest.objects.filter(nsot_off_id=user.pk)
    len_my_non_scheduled_ot_requests = len(my_non_scheduled_ot_requests)
    return render(request, "nsot_page.html", {'my_non_scheduled_ot_requests': my_non_scheduled_ot_requests, 'len_my_non_scheduled_ot_requests': len_my_non_scheduled_ot_requests})
    
@login_required()
def submit_nsot_request(request):
    if request.method == "POST":
        nsot_req_form = NonScheduledOvertimeRequestForm(request.POST, request.FILES)
        if nsot_req_form.is_valid():
            nsot_req_form.instance.nsot_off_id = request.user
            if nsot_req_form.instance.nsot_start_time > nsot_req_form.instance.nsot_end_time:
                messages.error(request, "The start time must be before the finish time.")
                return render(request, "submit_nsot_request.html", {'nsot_req_form': nsot_req_form})
            else:
                nsot_request = nsot_req_form.save()
                date_time_start = datetime.datetime.combine(nsot_request.nsot_date, nsot_request.nsot_start_time)
                date_time_end = datetime.datetime.combine(nsot_request.nsot_date, nsot_request.nsot_end_time)
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