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