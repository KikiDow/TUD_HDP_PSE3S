{"filter":false,"title":"views.py","tooltip":"/overtime/views.py","undoManager":{"mark":72,"position":72,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":2},{"start":{"row":0,"column":0},"end":{"row":8,"column":43},"action":"insert","lines":["from django.shortcuts import render, redirect, get_object_or_404","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from django.conf import settings","from .models import AllowancesRequest, NonScheduledOvertimeRequest, ShortOvertime, OvertimePerQtr, AvailabilitySheet, ShortTermAvailabilty, Overtime","from .forms import AllowancesRequestForm, NonScheduledOvertimeRequestForm, RejectAllowanceRequestForm, RejectNSOTForm, AvailabilitySheetForm, AssignOvertimeDateForm, AssignRecallStaffForm, AssignRequireStaffForm","import datetime","from annual_leave.utils import getLeaveAmount","from .utils import getQtrDateIn, getNextQtr"]}],[{"start":{"row":11,"column":0},"end":{"row":13,"column":48},"action":"insert","lines":["@login_required()","def overtime_page(request):","    return render(request, \"overtime_page.html\")"],"id":3}],[{"start":{"row":13,"column":48},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":15,"column":0},"end":{"row":20,"column":144},"action":"insert","lines":["@login_required()","def allowances_page(request):","    user = request.user","    allowance_requests = AllowancesRequest.objects.filter(allow_req_off_id=user.pk)","    len_allowance_requests = len(allowance_requests)","    return render(request, \"allowances_page.html\", {'allowance_requests': allowance_requests, 'len_allowance_requests': len_allowance_requests})"],"id":6}],[{"start":{"row":20,"column":144},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":8}],[{"start":{"row":22,"column":0},"end":{"row":69,"column":103},"action":"insert","lines":["@login_required()","def submit_allowance_request(request):","    if request.method == \"POST\":","        allowance_req_form = AllowancesRequestForm(request.POST, request.FILES)","        if allowance_req_form.is_valid():","            allowance_req_form.instance.allow_req_off_id = request.user","            if allowance_req_form.instance.claiming_food_for_prisoner_expense == True:","                if allowance_req_form.instance.food_for_prisoner_amount is None:","                    messages.error(request, \"You must include the cost of the prisoner's meal to claim this expense.\")","                    return render(request, \"submit_allowance_request.html\", {'allowance_req_form': allowance_req_form})","                elif allowance_req_form.instance.receipt_for_prisoner_food is False:","                    messages.error(request, \"You must provide a photograph of the receipt for the prisoner's meal to claim this expense.\")","                    return render(request, \"submit_allowance_request.html\", {'allowance_req_form': allowance_req_form})","                else:","                    allowance_request = allowance_req_form.save()","                    total_claim_amount = 0.0","                    if allowance_request.claiming_breakfast_allowance == True:","                        total_claim_amount += settings.BREAKFAST_ALLOWANCE","                    if allowance_request.claiming_dinner_allowance == True:","                        total_claim_amount += settings.DINNER_ALLOWANCE","                    if allowance_request.claiming_tea_allowance == True:","                        total_claim_amount += settings.TEA_ALLOWANCE","                    if allowance_request.claiming_plain_clothes_allowance == True:","                        total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE","                    if allowance_request.claiming_food_for_prisoner_expense == True:","                        total_claim_amount += allowance_request.food_for_prisoner_amount","                    allowance_request.claim_total = total_claim_amount","                    allowance_request.save()","                    return redirect(view_allowance_request, allowance_request.pk)","            else:","                allowance_request = allowance_req_form.save()","                total_claim_amount = 0.0","                if allowance_request.claiming_breakfast_allowance == True:","                    total_claim_amount += settings.BREAKFAST_ALLOWANCE","                if allowance_request.claiming_dinner_allowance == True:","                    total_claim_amount += settings.DINNER_ALLOWANCE","                if allowance_request.claiming_tea_allowance == True:","                    total_claim_amount += settings.TEA_ALLOWANCE","                if allowance_request.claiming_plain_clothes_allowance == True:","                    total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE","                if allowance_request.claiming_food_for_prisoner_expense == True:","                    total_claim_amount += allowance_request.food_for_prisoner_amount","                allowance_request.claim_total = total_claim_amount","                allowance_request.save()","                return redirect(view_allowance_request, allowance_request.pk)","    else:","        allowance_req_form = AllowancesRequestForm()","    return render(request, \"submit_allowance_request.html\", {'allowance_req_form': allowance_req_form})"],"id":9}],[{"start":{"row":69,"column":103},"end":{"row":70,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]},{"start":{"row":70,"column":4},"end":{"row":71,"column":0},"action":"insert","lines":["",""]},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"remove","lines":["    "],"id":11}],[{"start":{"row":71,"column":0},"end":{"row":75,"column":99},"action":"insert","lines":["@login_required()    ","def view_allowance_request(request, pk):","    allow_req_to_view = get_object_or_404(AllowancesRequest, pk=pk)","    allow_req_to_view.save()","    return render(request, \"view_allowance_request.html\", {'allow_req_to_view': allow_req_to_view})"],"id":12}],[{"start":{"row":75,"column":99},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"insert","lines":["    "]},{"start":{"row":76,"column":4},"end":{"row":77,"column":0},"action":"insert","lines":["",""]},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"remove","lines":["    "],"id":14}],[{"start":{"row":77,"column":0},"end":{"row":108,"column":151},"action":"insert","lines":["@login_required()","def edit_allowance_request(request, pk):","    allow_req_for_editing = get_object_or_404(AllowancesRequest, pk=pk) if pk else None","    if request.method == \"POST\":","        edit_allow_req_form = AllowancesRequestForm(request.POST, request.FILES, instance=allow_req_for_editing)","        if edit_allow_req_form.is_valid():","            if edit_allow_req_form.instance.claiming_food_for_prisoner_expense == True:","                if edit_allow_req_form.instance.food_for_prisoner_amount is None:","                    messages.error(request, \"You must include the cost of the prisoner's meal to claim this expense.\")","                    return render(request, \"edit_allowance_request.html\", {'edit_allow_req_form': edit_allow_req_form})","                elif edit_allow_req_form.instance.receipt_for_prisoner_food is False:","                    messages.error(request, \"You must provide a photograph of the receipt for the prisoner's meal to claim this expense.\")","                    return render(request, \"edit_allowance_request.html\", {'edit_allow_req_form': edit_allow_req_form})","                else:","                    allow_req_for_editing = edit_allow_req_form.save()","                    total_claim_amount = 0.0","                    if allow_req_for_editing.claiming_breakfast_allowance == True:","                        total_claim_amount += settings.BREAKFAST_ALLOWANCE","                    if allow_req_for_editing.claiming_dinner_allowance == True:","                        total_claim_amount += settings.DINNER_ALLOWANCE","                    if allow_req_for_editing.claiming_tea_allowance == True:","                        total_claim_amount += settings.TEA_ALLOWANCE","                    if allow_req_for_editing.claiming_plain_clothes_allowance == True:","                        total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE","                    if allow_req_for_editing.claiming_food_for_prisoner_expense == True:","                        total_claim_amount += allow_req_for_editing.food_for_prisoner_amount","                    allow_req_for_editing.claim_total = total_claim_amount","                    allow_req_for_editing.save()","                    return redirect(view_allowance_request, allow_req_for_editing.pk)","    else:","        edit_allow_req_form = AllowancesRequestForm(instance=allow_req_for_editing)","    return render(request, \"edit_allowance_request.html\", {'allow_req_for_editing': allow_req_for_editing, 'edit_allow_req_form': edit_allow_req_form})"],"id":15}],[{"start":{"row":108,"column":151},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]},{"start":{"row":109,"column":4},"end":{"row":110,"column":0},"action":"insert","lines":["",""]},{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"remove","lines":["    "],"id":17}],[{"start":{"row":110,"column":0},"end":{"row":115,"column":36},"action":"insert","lines":["@login_required()","def delete_allowance_request(request, pk):","    allowance_req_for_deletion = AllowancesRequest.objects.get(pk=pk)","    allowance_req_for_deletion.delete()","    messages.success(request, \"You have successfully deleted this allowance request.\")","    return redirect(allowances_page)"],"id":18}],[{"start":{"row":115,"column":36},"end":{"row":116,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":116,"column":0},"end":{"row":116,"column":4},"action":"insert","lines":["    "]},{"start":{"row":116,"column":4},"end":{"row":117,"column":0},"action":"insert","lines":["",""]},{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":117,"column":0},"end":{"row":122,"column":176},"action":"insert","lines":["@login_required()","def view_staff_allowance_requests(request):","    user = request.user","    staff_allowance_requests = AllowancesRequest.objects.filter(allow_req_checked_by_validator=False).exclude(allow_req_off_id=user.pk)","    length_of_staff_allow_req = len(staff_allowance_requests)","    return render(request, \"view_staff_allowance_requests.html\", {'staff_allowance_requests': staff_allowance_requests, 'length_of_staff_allow_req': length_of_staff_allow_req})"],"id":21}],[{"start":{"row":122,"column":176},"end":{"row":123,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"insert","lines":["    "]},{"start":{"row":123,"column":4},"end":{"row":124,"column":0},"action":"insert","lines":["",""]},{"start":{"row":124,"column":0},"end":{"row":124,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":4},"action":"remove","lines":["    "],"id":23}],[{"start":{"row":124,"column":0},"end":{"row":132,"column":52},"action":"insert","lines":["@login_required()","def accept_allowance_request(request, pk):","    allow_req_being_accepted = AllowancesRequest.objects.get(pk=pk)","    allow_req_being_accepted.allow_req_checked_by_validator = True","    allow_req_being_accepted.allow_req_accepted = True","    allow_req_being_accepted.save()","    #NOTIFICATION TO APPLCANT THAT ALLOWANCE REQUEST HAS BEEN ACCEPTED.","    messages.success(request, \"You have accepted this allowance request.\")","    return redirect('view_staff_allowance_requests')"],"id":24}],[{"start":{"row":8,"column":43},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":40},"action":"insert","lines":["from notifications.signals import notify"],"id":26}],[{"start":{"row":131,"column":71},"end":{"row":132,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":132,"column":4},"end":{"row":132,"column":152},"action":"insert","lines":["notify.send(request.user, recipient=fm_being_accepted.fm_officer_id, verb=\" has accepted your Force Majeure application: \" + str(fm_being_accepted))"],"id":28}],[{"start":{"row":132,"column":40},"end":{"row":132,"column":57},"action":"remove","lines":["fm_being_accepted"],"id":29},{"start":{"row":132,"column":40},"end":{"row":132,"column":64},"action":"insert","lines":["allow_req_being_accepted"]}],[{"start":{"row":132,"column":65},"end":{"row":132,"column":78},"action":"remove","lines":["fm_officer_id"],"id":30},{"start":{"row":132,"column":65},"end":{"row":132,"column":81},"action":"insert","lines":["allow_req_off_id"]}],[{"start":{"row":132,"column":132},"end":{"row":132,"column":133},"action":"remove","lines":["n"],"id":31},{"start":{"row":132,"column":131},"end":{"row":132,"column":132},"action":"remove","lines":["o"]},{"start":{"row":132,"column":130},"end":{"row":132,"column":131},"action":"remove","lines":["i"]},{"start":{"row":132,"column":129},"end":{"row":132,"column":130},"action":"remove","lines":["t"]},{"start":{"row":132,"column":128},"end":{"row":132,"column":129},"action":"remove","lines":["a"]},{"start":{"row":132,"column":127},"end":{"row":132,"column":128},"action":"remove","lines":["c"]},{"start":{"row":132,"column":126},"end":{"row":132,"column":127},"action":"remove","lines":["i"]},{"start":{"row":132,"column":125},"end":{"row":132,"column":126},"action":"remove","lines":["l"]},{"start":{"row":132,"column":124},"end":{"row":132,"column":125},"action":"remove","lines":["p"]},{"start":{"row":132,"column":123},"end":{"row":132,"column":124},"action":"remove","lines":["p"]},{"start":{"row":132,"column":122},"end":{"row":132,"column":123},"action":"remove","lines":["a"]},{"start":{"row":132,"column":121},"end":{"row":132,"column":122},"action":"remove","lines":[" "]},{"start":{"row":132,"column":120},"end":{"row":132,"column":121},"action":"remove","lines":["e"]},{"start":{"row":132,"column":119},"end":{"row":132,"column":120},"action":"remove","lines":["r"]},{"start":{"row":132,"column":118},"end":{"row":132,"column":119},"action":"remove","lines":["u"]},{"start":{"row":132,"column":117},"end":{"row":132,"column":118},"action":"remove","lines":["e"]},{"start":{"row":132,"column":116},"end":{"row":132,"column":117},"action":"remove","lines":["j"]},{"start":{"row":132,"column":115},"end":{"row":132,"column":116},"action":"remove","lines":["a"]},{"start":{"row":132,"column":114},"end":{"row":132,"column":115},"action":"remove","lines":["M"]},{"start":{"row":132,"column":113},"end":{"row":132,"column":114},"action":"remove","lines":[" "]},{"start":{"row":132,"column":112},"end":{"row":132,"column":113},"action":"remove","lines":["e"]},{"start":{"row":132,"column":111},"end":{"row":132,"column":112},"action":"remove","lines":["c"]},{"start":{"row":132,"column":110},"end":{"row":132,"column":111},"action":"remove","lines":["r"]},{"start":{"row":132,"column":109},"end":{"row":132,"column":110},"action":"remove","lines":["o"]},{"start":{"row":132,"column":108},"end":{"row":132,"column":109},"action":"remove","lines":["F"]}],[{"start":{"row":132,"column":108},"end":{"row":132,"column":109},"action":"insert","lines":["a"],"id":32},{"start":{"row":132,"column":109},"end":{"row":132,"column":110},"action":"insert","lines":["l"]},{"start":{"row":132,"column":110},"end":{"row":132,"column":111},"action":"insert","lines":["l"]},{"start":{"row":132,"column":111},"end":{"row":132,"column":112},"action":"insert","lines":["o"]},{"start":{"row":132,"column":112},"end":{"row":132,"column":113},"action":"insert","lines":["w"]},{"start":{"row":132,"column":113},"end":{"row":132,"column":114},"action":"insert","lines":["a"]},{"start":{"row":132,"column":114},"end":{"row":132,"column":115},"action":"insert","lines":["n"]},{"start":{"row":132,"column":115},"end":{"row":132,"column":116},"action":"insert","lines":["c"]},{"start":{"row":132,"column":116},"end":{"row":132,"column":117},"action":"insert","lines":["e"]}],[{"start":{"row":132,"column":117},"end":{"row":132,"column":118},"action":"insert","lines":[" "],"id":33},{"start":{"row":132,"column":118},"end":{"row":132,"column":119},"action":"insert","lines":["r"]},{"start":{"row":132,"column":119},"end":{"row":132,"column":120},"action":"insert","lines":["e"]}],[{"start":{"row":132,"column":120},"end":{"row":132,"column":121},"action":"insert","lines":["q"],"id":34},{"start":{"row":132,"column":121},"end":{"row":132,"column":122},"action":"insert","lines":["u"]},{"start":{"row":132,"column":122},"end":{"row":132,"column":123},"action":"insert","lines":["e"]},{"start":{"row":132,"column":123},"end":{"row":132,"column":124},"action":"insert","lines":["s"]},{"start":{"row":132,"column":124},"end":{"row":132,"column":125},"action":"insert","lines":["t"]}],[{"start":{"row":132,"column":125},"end":{"row":132,"column":126},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":132,"column":136},"end":{"row":132,"column":153},"action":"remove","lines":["fm_being_accepted"],"id":36},{"start":{"row":132,"column":136},"end":{"row":132,"column":160},"action":"insert","lines":["allow_req_being_accepted"]}],[{"start":{"row":132,"column":160},"end":{"row":132,"column":161},"action":"insert","lines":["."],"id":37}],[{"start":{"row":132,"column":161},"end":{"row":132,"column":175},"action":"insert","lines":["allow_req_date"],"id":38}],[{"start":{"row":134,"column":52},"end":{"row":135,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":135,"column":0},"end":{"row":135,"column":4},"action":"insert","lines":["    "]},{"start":{"row":135,"column":4},"end":{"row":136,"column":0},"action":"insert","lines":["",""]},{"start":{"row":136,"column":0},"end":{"row":136,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":136,"column":0},"end":{"row":136,"column":4},"action":"remove","lines":["    "],"id":40}],[{"start":{"row":136,"column":0},"end":{"row":150,"column":159},"action":"insert","lines":["@login_required()","def reject_allowance_request(request, pk):","    allow_req_being_rejected = AllowancesRequest.objects.get(pk=pk)","    if request.method == \"POST\":","        allow_req_reject_form = RejectAllowanceRequestForm(request.POST, request.FILES, instance=allow_req_being_rejected)","        if allow_req_reject_form.is_valid():","            allow_req_being_rejected = allow_req_reject_form.save()","            allow_req_being_rejected.allow_req_checked_by_validator = True","            allow_req_being_rejected.allow_req_accepted = False","            allow_req_being_rejected.save()","            #NOTIFICATION TO APPLCANT THAT ALLOWANCE REQUEST HAS BEEN ACCEPTED.","            messages.success(request, \"You have rejected this allowance request.\")","    else:","        allow_req_reject_form = RejectAllowanceRequestForm(instance=allow_req_being_rejected)","    return render(request, \"reject_allow_request.html\", {'allow_req_being_rejected': allow_req_being_rejected, 'allow_req_reject_form': allow_req_reject_form})"],"id":41}],[{"start":{"row":146,"column":79},"end":{"row":147,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":147,"column":0},"end":{"row":147,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":147,"column":12},"end":{"row":147,"column":185},"action":"insert","lines":["notify.send(request.user, recipient=allow_req_being_accepted.allow_req_off_id, verb=\" has accepted your allowance request : \" + str(allow_req_being_accepted.allow_req_date))"],"id":43}],[{"start":{"row":146,"column":77},"end":{"row":146,"column":78},"action":"remove","lines":["D"],"id":44},{"start":{"row":146,"column":76},"end":{"row":146,"column":77},"action":"remove","lines":["E"]},{"start":{"row":146,"column":75},"end":{"row":146,"column":76},"action":"remove","lines":["T"]},{"start":{"row":146,"column":74},"end":{"row":146,"column":75},"action":"remove","lines":["P"]},{"start":{"row":146,"column":73},"end":{"row":146,"column":74},"action":"remove","lines":["E"]},{"start":{"row":146,"column":72},"end":{"row":146,"column":73},"action":"remove","lines":["C"]},{"start":{"row":146,"column":71},"end":{"row":146,"column":72},"action":"remove","lines":["C"]},{"start":{"row":146,"column":70},"end":{"row":146,"column":71},"action":"remove","lines":["A"]}],[{"start":{"row":146,"column":70},"end":{"row":146,"column":71},"action":"insert","lines":["R"],"id":45},{"start":{"row":146,"column":71},"end":{"row":146,"column":72},"action":"insert","lines":["E"]},{"start":{"row":146,"column":72},"end":{"row":146,"column":73},"action":"insert","lines":["J"]},{"start":{"row":146,"column":73},"end":{"row":146,"column":74},"action":"insert","lines":["E"]},{"start":{"row":146,"column":74},"end":{"row":146,"column":75},"action":"insert","lines":["C"]},{"start":{"row":146,"column":75},"end":{"row":146,"column":76},"action":"insert","lines":["T"]},{"start":{"row":146,"column":76},"end":{"row":146,"column":77},"action":"insert","lines":["E"]},{"start":{"row":146,"column":77},"end":{"row":146,"column":78},"action":"insert","lines":["D"]}],[{"start":{"row":147,"column":48},"end":{"row":147,"column":72},"action":"remove","lines":["allow_req_being_accepted"],"id":46},{"start":{"row":147,"column":48},"end":{"row":147,"column":72},"action":"insert","lines":["allow_req_being_rejected"]}],[{"start":{"row":147,"column":144},"end":{"row":147,"column":168},"action":"remove","lines":["allow_req_being_accepted"],"id":47},{"start":{"row":147,"column":144},"end":{"row":147,"column":168},"action":"insert","lines":["allow_req_being_rejected"]}],[{"start":{"row":147,"column":106},"end":{"row":147,"column":107},"action":"remove","lines":["p"],"id":48},{"start":{"row":147,"column":105},"end":{"row":147,"column":106},"action":"remove","lines":["e"]},{"start":{"row":147,"column":104},"end":{"row":147,"column":105},"action":"remove","lines":["c"]},{"start":{"row":147,"column":103},"end":{"row":147,"column":104},"action":"remove","lines":["c"]},{"start":{"row":147,"column":102},"end":{"row":147,"column":103},"action":"remove","lines":["a"]},{"start":{"row":147,"column":101},"end":{"row":147,"column":102},"action":"remove","lines":[" "]},{"start":{"row":147,"column":100},"end":{"row":147,"column":101},"action":"remove","lines":["s"]},{"start":{"row":147,"column":99},"end":{"row":147,"column":100},"action":"remove","lines":["a"]},{"start":{"row":147,"column":98},"end":{"row":147,"column":99},"action":"remove","lines":["h"]}],[{"start":{"row":147,"column":98},"end":{"row":147,"column":99},"action":"insert","lines":["H"],"id":49},{"start":{"row":147,"column":99},"end":{"row":147,"column":100},"action":"insert","lines":["A"]},{"start":{"row":147,"column":100},"end":{"row":147,"column":101},"action":"insert","lines":["S"]}],[{"start":{"row":147,"column":101},"end":{"row":147,"column":102},"action":"insert","lines":[" "],"id":50}],[{"start":{"row":147,"column":101},"end":{"row":147,"column":102},"action":"remove","lines":[" "],"id":51},{"start":{"row":147,"column":100},"end":{"row":147,"column":101},"action":"remove","lines":["S"]},{"start":{"row":147,"column":99},"end":{"row":147,"column":100},"action":"remove","lines":["A"]},{"start":{"row":147,"column":98},"end":{"row":147,"column":99},"action":"remove","lines":["H"]}],[{"start":{"row":147,"column":98},"end":{"row":147,"column":99},"action":"insert","lines":["h"],"id":52},{"start":{"row":147,"column":99},"end":{"row":147,"column":100},"action":"insert","lines":["a"]},{"start":{"row":147,"column":100},"end":{"row":147,"column":101},"action":"insert","lines":["s"]}],[{"start":{"row":147,"column":101},"end":{"row":147,"column":102},"action":"insert","lines":[" "],"id":53},{"start":{"row":147,"column":102},"end":{"row":147,"column":103},"action":"insert","lines":["r"]},{"start":{"row":147,"column":103},"end":{"row":147,"column":104},"action":"insert","lines":["e"]},{"start":{"row":147,"column":104},"end":{"row":147,"column":105},"action":"insert","lines":["j"]},{"start":{"row":147,"column":105},"end":{"row":147,"column":106},"action":"insert","lines":["e"]},{"start":{"row":147,"column":106},"end":{"row":147,"column":107},"action":"insert","lines":["c"]},{"start":{"row":147,"column":107},"end":{"row":147,"column":108},"action":"insert","lines":["t"]},{"start":{"row":147,"column":108},"end":{"row":147,"column":109},"action":"insert","lines":["e"]}],[{"start":{"row":147,"column":108},"end":{"row":147,"column":109},"action":"remove","lines":["e"],"id":54},{"start":{"row":147,"column":107},"end":{"row":147,"column":108},"action":"remove","lines":["t"]}],[{"start":{"row":151,"column":159},"end":{"row":152,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":152,"column":0},"end":{"row":152,"column":4},"action":"insert","lines":["    "]},{"start":{"row":152,"column":4},"end":{"row":153,"column":0},"action":"insert","lines":["",""]},{"start":{"row":153,"column":0},"end":{"row":153,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":153,"column":0},"end":{"row":153,"column":4},"action":"remove","lines":["    "],"id":56},{"start":{"row":152,"column":4},"end":{"row":153,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":152,"column":4},"end":{"row":153,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":153,"column":0},"end":{"row":153,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":153,"column":0},"end":{"row":153,"column":4},"action":"remove","lines":["    "],"id":58}],[{"start":{"row":153,"column":0},"end":{"row":158,"column":178},"action":"insert","lines":["@login_required()","def non_scheduled_ot_page(request):","    user = request.user","    my_non_scheduled_ot_requests = NonScheduledOvertimeRequest.objects.filter(nsot_off_id=user.pk)","    len_my_non_scheduled_ot_requests = len(my_non_scheduled_ot_requests)","    return render(request, \"nsot_page.html\", {'my_non_scheduled_ot_requests': my_non_scheduled_ot_requests, 'len_my_non_scheduled_ot_requests': len_my_non_scheduled_ot_requests})"],"id":59}],[{"start":{"row":158,"column":178},"end":{"row":159,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":159,"column":0},"end":{"row":159,"column":4},"action":"insert","lines":["    "]},{"start":{"row":159,"column":4},"end":{"row":160,"column":0},"action":"insert","lines":["",""]},{"start":{"row":160,"column":0},"end":{"row":160,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":160,"column":0},"end":{"row":160,"column":4},"action":"remove","lines":["    "],"id":61}],[{"start":{"row":160,"column":0},"end":{"row":180,"column":88},"action":"insert","lines":["@login_required()","def submit_nsot_request(request):","    if request.method == \"POST\":","        nsot_req_form = NonScheduledOvertimeRequestForm(request.POST, request.FILES)","        if nsot_req_form.is_valid():","            nsot_req_form.instance.nsot_off_id = request.user","            if nsot_req_form.instance.nsot_start_time > nsot_req_form.instance.nsot_end_time:","                messages.error(request, \"The start time must be before the finish time.\")","                return render(request, \"submit_nsot_request.html\", {'nsot_req_form': nsot_req_form})","            else:","                nsot_request = nsot_req_form.save()","                date_time_start = datetime.datetime.combine(nsot_request.nsot_date, nsot_request.nsot_start_time)","                date_time_end = datetime.datetime.combine(nsot_request.nsot_date, nsot_request.nsot_end_time)","                nsot_difference_as_delta = date_time_end - date_time_start","                nsot_request.ot_hours_claimed = getLeaveAmount(nsot_difference_as_delta)","                nsot_request.save()","                messages.success(request, \"Non Scheduled Overtime Request successfully submitted.\")","                return redirect(view_non_scheduled_overtime_request, nsot_request.id)","    else:","        nsot_req_form = NonScheduledOvertimeRequestForm()","    return render(request, \"submit_nsot_request.html\", {'nsot_req_form': nsot_req_form})"],"id":62}],[{"start":{"row":180,"column":88},"end":{"row":181,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":181,"column":0},"end":{"row":181,"column":4},"action":"insert","lines":["    "]},{"start":{"row":181,"column":4},"end":{"row":182,"column":0},"action":"insert","lines":["",""]},{"start":{"row":182,"column":0},"end":{"row":182,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":182,"column":0},"end":{"row":182,"column":4},"action":"remove","lines":["    "],"id":64}],[{"start":{"row":182,"column":0},"end":{"row":186,"column":92},"action":"insert","lines":["@login_required()","def view_non_scheduled_overtime_request(request, pk):","    nsot_req_to_view = get_object_or_404(NonScheduledOvertimeRequest, pk=pk)","    nsot_req_to_view.save()","    return render(request, \"view_nsot_request.html\", {'nsot_req_to_view': nsot_req_to_view})"],"id":65}],[{"start":{"row":186,"column":92},"end":{"row":187,"column":0},"action":"insert","lines":["",""],"id":66},{"start":{"row":187,"column":0},"end":{"row":187,"column":4},"action":"insert","lines":["    "]},{"start":{"row":187,"column":4},"end":{"row":188,"column":0},"action":"insert","lines":["",""]},{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"remove","lines":["    "],"id":67}],[{"start":{"row":188,"column":0},"end":{"row":193,"column":42},"action":"insert","lines":["@login_required()","def delete_nsot_request(request, pk):","    nsot_req_for_deletion = NonScheduledOvertimeRequest.objects.get(pk=pk)","    nsot_req_for_deletion.delete()","    messages.success(request, \"You have successfully deleted this non-scheduled overtime request.\")","    return redirect(non_scheduled_ot_page)"],"id":68}],[{"start":{"row":193,"column":42},"end":{"row":194,"column":0},"action":"insert","lines":["",""],"id":69},{"start":{"row":194,"column":0},"end":{"row":194,"column":4},"action":"insert","lines":["    "]},{"start":{"row":194,"column":4},"end":{"row":195,"column":0},"action":"insert","lines":["",""]},{"start":{"row":195,"column":0},"end":{"row":195,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":195,"column":0},"end":{"row":195,"column":4},"action":"remove","lines":["    "],"id":70}],[{"start":{"row":195,"column":0},"end":{"row":210,"column":134},"action":"insert","lines":["@login_required()","def edit_nsot_request(request, pk):","    nsot_req_for_editing = get_object_or_404(NonScheduledOvertimeRequest, pk=pk) if pk else None","    if request.method == \"POST\":","        edit_nsot_form = NonScheduledOvertimeRequestForm(request.POST, request.FILES, instance=nsot_req_for_editing)","        if edit_nsot_form.is_valid():","            if edit_nsot_form.instance.nsot_start_time > edit_nsot_form.instance.nsot_end_time:","                messages.error(request, \"The start date for the non scheduled overtime request must be before the end date.\")","                return render(request, \"edit_nsot_request.html\", {'edit_nsot_form': edit_nsot_form})","            else:","                nsot_req_for_editing = edit_nsot_form.save()","                messages.success(request, 'You have successfully made changes to this non scheduled overtime request.')","                return redirect(view_non_scheduled_overtime_request, nsot_req_for_editing.pk)","    else:","        edit_nsot_form = NonScheduledOvertimeRequestForm(instance=nsot_req_for_editing)","    return render(request, \"edit_nsot_request.html\", {'nsot_req_for_editing': nsot_req_for_editing, 'edit_nsot_form': edit_nsot_form})"],"id":71}],[{"start":{"row":210,"column":134},"end":{"row":211,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":211,"column":0},"end":{"row":211,"column":4},"action":"insert","lines":["    "]},{"start":{"row":211,"column":4},"end":{"row":212,"column":0},"action":"insert","lines":["",""]},{"start":{"row":212,"column":0},"end":{"row":212,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":212,"column":0},"end":{"row":212,"column":4},"action":"remove","lines":["    "],"id":73}],[{"start":{"row":212,"column":0},"end":{"row":217,"column":159},"action":"insert","lines":["@login_required()","def view_staff_nsot_requests(request):","    user = request.user","    staff_nsot_requests = NonScheduledOvertimeRequest.objects.filter(nsot_checked_by_validator=False).exclude(nsot_off_id=user.pk)","    length_of_staff_nsot_req = len(staff_nsot_requests)","    return render(request, \"view_staff_nsot_requests.html\", {'staff_nsot_requests': staff_nsot_requests, 'length_of_staff_nsot_req': length_of_staff_nsot_req})"],"id":74}]]},"ace":{"folds":[],"scrolltop":2682,"scrollleft":0,"selection":{"start":{"row":213,"column":4},"end":{"row":213,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605885205671,"hash":"c8e9bbb2634afd277e3adde87ad44f00da62783f"}