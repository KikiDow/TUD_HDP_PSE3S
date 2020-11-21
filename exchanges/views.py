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
    
@login_required()
def view_all_exchanges(request):
    user = request.user
    exchange_requests = ExchangeRequest.objects.filter(Q(exchanging_req_officer=user) | Q(replacing_req_officer=user)).filter(swap_cancelled=False)
    #Started: Awaiting Replacement officer reply
    exchanges_req_started = exchange_requests.filter(exchanging_req_officer=user).filter(ro_proceed_with_swap=False)
    len_exchange_req_started = len(exchanges_req_started)
    #Awaiting my reply:
    exchanges_req_awaiting_reply = exchange_requests.filter(replacing_req_officer=user).filter(ro_proceed_with_swap=False)
    len_exchange_req_awaiting_reply = len(exchanges_req_awaiting_reply)
    #Awaiting Exchanging Officers Confirmation.
    exchange_reqs_awaiting_eo_confirm = exchange_requests.filter(replacing_req_officer=user).filter(ro_proceed_with_swap=True)
    len_exchange_req_awaiting_eo_confirm = len(exchange_reqs_awaiting_eo_confirm)
    #Awaiting my confirmation:
    exchanges_req_awaiting_confirmation = exchange_requests.filter(exchanging_req_officer=user).filter(eo_proceed_with_swap=False).filter(ro_proceed_with_swap=True)
    len_exchange_req_waiting_confirm = len(exchanges_req_awaiting_confirmation)
    
    return render(request, "view_all_exchanges.html", {'exchanges_req_started': exchanges_req_started, 'exchanges_req_awaiting_reply': exchanges_req_awaiting_reply, 'exchange_reqs_awaiting_eo_confirm': exchange_reqs_awaiting_eo_confirm, 'exchanges_req_awaiting_confirmation': exchanges_req_awaiting_confirmation, 'len_exchange_req_started': len_exchange_req_started, 'len_exchange_req_awaiting_reply': len_exchange_req_awaiting_reply, 'len_exchange_req_awaiting_eo_confirm': len_exchange_req_awaiting_eo_confirm, 'len_exchange_req_waiting_confirm': len_exchange_req_waiting_confirm})
    
@login_required()
def previous_exchanges(request):
    user = request.user
    exchange_requests = ExchangeRequest.objects.filter(Q(exchanging_req_officer=user) | Q(replacing_req_officer=user)).filter(swap_cancelled=False)
    #cancelled swaps:
    exchange_reqs_cancelled = exchange_requests.filter(swap_cancelled=True)
    len_cancelled_exchanges = len(exchange_reqs_cancelled)
    #Previous Exchanges
    todays_date = dt.date.today()
    previous_exchange_reqs = exchange_requests.filter(swap_confirmed=True).filter(Q(exchange_req_date__lt=todays_date) & Q(replacing_req_date__lt=todays_date))
    len_previous_exchange_reqs = len(previous_exchange_reqs)
    
    return render(request, "view_previous_exchanges.html", {'exchange_reqs_cancelled': exchange_reqs_cancelled, 'previous_exchange_reqs': previous_exchange_reqs,'len_cancelled_exchanges': len_cancelled_exchanges, 'len_previous_exchange_reqs': len_previous_exchange_reqs})
    
    
    