{"filter":false,"title":"views.py","tooltip":"/annual_leave/views.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":9,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, get_object_or_404","from .utils import getCurrentYear, getLeaveAmount","from .models import AnnualLeave, AnnualLeaveRequest, ShortTermAnnualLeaveRequest","import datetime","from django.contrib.auth.decorators import login_required","from .forms import AnnualLeaveRequestForm, ShortTermAnnualLeaveRequestForm, AnnualLeaveRequestRejectForm, ShortTermLeaveRequestRejectForm","from django.contrib import messages","from account.models import Account","from itertools import chain","from clocking.models import Roster, Shift"]}],[{"start":{"row":9,"column":41},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["# Create your views here.","@login_required()","def annual_leave_page(request):","    current_year = getCurrentYear()","    officer_user = request.user","    off = Account.objects.get(pk=officer_user.pk)","    off_current_leave_total = off.current_leave_total","    officers_leave = AnnualLeave.objects.filter(al_officer_id=officer_user.pk).filter(al_date__year=current_year)","    todays_date = datetime.date.today()","    upcoming_leave = []","    previous_leave = []","    for leave in officers_leave:","        if leave.al_date <= todays_date:","            previous_leave.append(leave)","        else:","            upcoming_leave.append(leave)","            ","    length_upcoming_leave = len(upcoming_leave)","    length_previous_leave = len(previous_leave)","    ","    return render(request, \"annual_leave.html\", {'upcoming_leave': upcoming_leave, 'previous_leave': previous_leave, 'length_previous_leave': length_previous_leave, 'length_upcoming_leave': length_upcoming_leave, 'off_current_leave_total': off_current_leave_total})","    "],"id":4}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "],"id":5},{"start":{"row":31,"column":265},"end":{"row":32,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":93,"scrollleft":0,"selection":{"start":{"row":13,"column":4},"end":{"row":13,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1605728763301,"hash":"c9087c6ca196299133320214689ea5618ce8cc9d"}