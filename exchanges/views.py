from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Exchange, ExchangeRequest, Post, Like
import datetime as dt
from datetime import datetime
from .forms import SubmitExchangeRequestExchangingOfficerForm, SubmitExchangeRequestReplacingOfficerForm, SubmitExchangeRequestExchangingOfficerCheckForm, PostForm, CancelExchangeRequestForm
from clocking.models import Roster, Shift
from notifications.signals import notify

# Create your views here.
@login_required()
def exchanges_page(request):
    user = request.user
    todays_date = dt.date.today()
    exchanges = Exchange.objects.filter(Q(exchanging_officer=user) | Q(replacing_officer=user)).filter(Q(exchange_date__gte=todays_date) | Q(replacement_date__gte=todays_date))
    len_exchanges = len(exchanges)
    return render(request, "exchanges_page.html", {'exchanges': exchanges, 'len_exchanges': len_exchanges})
    
@login_required()    
def submit_exchange_exchange_off(request):
    if request.method == "POST":
        submit_exchange_exchange_off_form = SubmitExchangeRequestExchangingOfficerForm(request.POST, request.FILES)
        exchange_req_date = request.POST.get('exchange_req_date')
        submit_exchange_exchange_off_form.fields['exchange_req_date'].choices = [(exchange_req_date, exchange_req_date)]
        if submit_exchange_exchange_off_form.is_valid():
            submit_exchange_exchange_off_form.instance.exchanging_req_officer = request.user
            '''
            date_as_string = submit_exchange_exchange_off_form.instance.exchange_req_date
            #convert string representation to datetime object.
            date_as_datetime = datetime.strptime(date_as_string, "%Y-%m-%d")
            #convert datetime object to date object.
            date_as_date_obj = dt.date(date_as_datetime.year, date_as_datetime.month, date_as_datetime.day)
            submit_exchange_exchange_off_form.instance.exchange_req_date = date_as_date_obj
            '''
            new_exchange_req = submit_exchange_exchange_off_form.save()

            exch_date = new_exchange_req.exchange_req_date
            roster_day = Roster.objects.get(roster_officer_id=new_exchange_req.exchanging_req_officer, roster_shift_date__contains=exch_date)
            newly_created_exch_req = ExchangeRequest.objects.get(pk=new_exchange_req.id)
            newly_created_exch_req.exchange_req_shift_label = roster_day.roster_shift_label
            newly_created_exch_req.save()
            messages.success(request, "Exchange Reguest successfully started.")
            #NOTIFICATION TO REPLACING OFFICER THAT EXCHANGE HAS BEEN STARTED.
            notify.send(newly_created_exch_req.exchanging_req_officer, recipient=newly_created_exch_req.replacing_req_officer, verb=" has begun an exchange request for : " + str(newly_created_exch_req.exchange_req_date))
            return redirect(exchanges_page)
    else:
        submit_exchange_exchange_off_form = SubmitExchangeRequestExchangingOfficerForm()
        
    return render(request, "submit_exchange_exchange_off.html", {'submit_exchange_exchange_off_form': submit_exchange_exchange_off_form})