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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            #NOTIFICATION TO REPLACING OFFICER THAT EXCHANGE HAS BEEN STARTED.
            notify.send(newly_created_exch_req.exchanging_req_officer, recipient=newly_created_exch_req.replacing_req_officer, verb=" has begun an exchange request for : " + str(newly_created_exch_req.exchange_req_date))
            messages.success(request, "Exchange Reguest successfully started.")
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
    
    
@login_required()
def submit_exchange_replacing_off_reply(request, pk):
    exchange_req_being_replied_to = ExchangeRequest.objects.get(pk=pk)
    if request.method == "POST":
        submit_exchange_replacing_off_form = SubmitExchangeRequestReplacingOfficerForm(request.POST, request.FILES, instance=exchange_req_being_replied_to)
        replacing_req_date = request.POST.get('replacing_req_date')
        submit_exchange_replacing_off_form.fields['replacing_req_date'].choices = [(replacing_req_date, replacing_req_date)]
        if submit_exchange_replacing_off_form.is_valid():
            new_exchange_req_replace_reply = submit_exchange_replacing_off_form.save()
            replace_date = new_exchange_req_replace_reply.replacing_req_date
            roster_day = Roster.objects.get(roster_officer_id=new_exchange_req_replace_reply.replacing_req_officer, roster_shift_date__contains=replace_date)
            newly_created_exch_req_reply = ExchangeRequest.objects.get(pk=new_exchange_req_replace_reply.id)
            newly_created_exch_req_reply.replacing_req_shift = roster_day.roster_shift_label
            newly_created_exch_req_reply.save()
            notify.send(newly_created_exch_req_reply.replacing_req_officer, recipient=newly_created_exch_req_reply.exchanging_req_officer, verb=" has replied to your exchange request : " + str(newly_created_exch_req_reply.exchange_req_date))
            messages.success(request, "You have successfully replied to this exchange request.")
            #NOTIFICATION TO EXCHANGING OFFICER THAT REPLY HAS BEEN SENT.
            return redirect(view_all_exchanges)
    else:
        submit_exchange_replacing_off_form = SubmitExchangeRequestReplacingOfficerForm(instance=exchange_req_being_replied_to)
    return render(request, "submit_exchange_replacing_off_reply.html", {'exchange_req_being_replied_to': exchange_req_being_replied_to, 'submit_exchange_replacing_off_form': submit_exchange_replacing_off_form})

@login_required()
def submit_exchange_exchange_off_confirm(request, pk):
    exchange_req_being_confirmed = ExchangeRequest.objects.get(pk=pk)
    if request.method == "POST":
        submit_exchange_req_confirm_form = SubmitExchangeRequestExchangingOfficerCheckForm(request.POST, request.FILES, instance=exchange_req_being_confirmed)
        if submit_exchange_req_confirm_form.is_valid():
            new_exchange_confirm = submit_exchange_req_confirm_form.save()
            if new_exchange_confirm.eo_proceed_with_swap == True:
                new_exchange_confirm.swap_confirmed = True
                new_exchange_confirm.save()
               
                if new_exchange_confirm.swap_confirmed == True:
                    associated_post = Post.objects.get(postee_id=new_exchange_confirm.exchanging_req_officer.id, possible_exchange_date=new_exchange_confirm.exchange_req_date)
                    if associated_post.exists():
                        associated_post.post_led_to_exchange = True
                        associated_post.save()
                    else:
                        pass
                    
                roster_exch_day = Roster.objects.get(roster_officer_id=new_exchange_confirm.exchanging_req_officer, roster_shift_date__contains=new_exchange_confirm.exchange_req_date)
                roster_replace_day = Roster.objects.get(roster_officer_id=new_exchange_confirm.replacing_req_officer, roster_shift_date__contains=new_exchange_confirm.replacing_req_date)
                exch_shift = Shift.objects.get(shift_label=roster_exch_day.roster_shift_label)
                print(exch_shift)
                replace_shift = Shift.objects.get(shift_label=roster_replace_day.roster_shift_label)
                print(replace_shift)
                
                new_exchange = Exchange(exchanging_officer=new_exchange_confirm.exchanging_req_officer, exchange_date=new_exchange_confirm.exchange_req_date, exchange_shift=exch_shift, replacing_officer=new_exchange_confirm.replacing_req_officer, replacement_date=new_exchange_confirm.replacing_req_date, replacement_shift=replace_shift)
                new_exchange.save()
                #notification to replacing officer of confirmation.
                notify.send(new_exchange.exchanging_officer, recipient=new_exchange.replacing_officer, verb=" has confirmed your exchange for : " + str(new_exchange.exchange_date) + " and " + str(new_exchange.replacement_date))
                messages.success(request, "Your exchange with " + str(new_exchange_confirm.replacing_req_officer) + " has been confirmed.")
                return redirect(exchanges_page)
    else:
        submit_exchange_req_confirm_form = SubmitExchangeRequestExchangingOfficerCheckForm(instance=exchange_req_being_confirmed)
    return render(request, "exchange_off_confirm.html", {'exchange_req_being_confirmed': exchange_req_being_confirmed, 'submit_exchange_req_confirm_form': submit_exchange_req_confirm_form})

@login_required()
def exchange_noticeboard(request):
    todays_date = dt.date.today()
    noticeboard_posts = Post.objects.filter(post_led_to_exchange=False).filter(possible_exchange_date__gt=todays_date)
    #
    likes = Like.objects.all()
    len_posts = len(noticeboard_posts)
    #Pagination
    page_number = 1
    page = request.GET.get('page', page_number)
    
    paginator = Paginator(noticeboard_posts, 2)
    try:
        noticeboard = paginator.page(page)
    except PageNotAnInteger:
        noticeboard = paginator.page(1)
    except EmptyPage:
        noticeboard = paginator.page(paginator.num_pages)
    return render(request, "exchange_noticeboard.html", {'noticeboard': noticeboard, 'likes': likes, 'len_posts': len_posts})
    
@login_required()
def submit_post(request):
    if request.method == "POST":
        submit_post_form = PostForm(request.POST, request.FILES)
        possible_exchange_date = request.POST.get('possible_exchange_date')
        submit_post_form.fields['possible_exchange_date'].choices = [(possible_exchange_date, possible_exchange_date)]
        if submit_post_form.is_valid():
            submit_post_form.instance.postee_id = request.user
            new_post = submit_post_form.save()
            roster_day_for_post = Roster.objects.get(roster_officer_id=new_post.postee_id, roster_shift_date__contains=new_post.possible_exchange_date)
            shift_for_post = Shift.objects.get(shift_label=roster_day_for_post.roster_shift_label)
            new_post.possible_exchange_shift_id = shift_for_post
            new_post.save()
            messages.success(request, "You have posted on the noticeboard.")
            return redirect(exchange_noticeboard)
    else:
        submit_post_form = PostForm()
    return render(request, "submit_post.html", {'submit_post_form': submit_post_form})
    
@login_required()
def like_post(request, pk):
    post_being_liked = Post.objects.get(pk=pk)
    post_being_liked.likes += 1
    post_being_liked.save()
    new_like = Like(post_liked=post_being_liked, post_liked_by=request.user)
    new_like.save()
    notify.send(new_like.post_liked_by, recipient=post_being_liked.postee_id, verb=" is interested in your post for : " + str(post_being_liked.possible_exchange_date))
    messages.success(request, "Post Liked !!")
    return redirect(exchange_noticeboard)
    
@login_required()
def cancel_exchange(request, pk):
    exchange_being_cancelled = ExchangeRequest.objects.get(pk=pk)
    if request.method == "POST":
        cancel_exchange_form = CancelExchangeRequestForm(request.POST, request.FILES, instance=exchange_being_cancelled)
        if cancel_exchange_form.is_valid():
            new_cancel_exchange = cancel_exchange_form.save()
            if new_cancel_exchange.exchanging_req_officer == request.user:
                #Notification to replacing offcier that swap is cancelled.
                notify.send(new_cancel_exchange.exchanging_req_officer, recipient=new_cancel_exchange.replacing_req_officer, verb=" has cancelled an exchange for : " + str(new_cancel_exchange.exchange_req_date))
            else:
                #Notifiction to exchanging officer that swap is cancelled.
                notify.send(new_cancel_exchange.replacing_req_officer, recipient=new_cancel_exchange.exchanging_req_officer, verb=" has cancelled an exchange for : " + str(new_cancel_exchange.exchange_req_date))
            
            messages.success(request, "Exchange Request Cancelled.")
            
            return redirect(exchanges_page)
    else:
        cancel_exchange_form = CancelExchangeRequestForm(instance=exchange_being_cancelled)
    return render(request, "cancel_exchange_request.html", {'exchange_being_cancelled': exchange_being_cancelled, 'cancel_exchange_form': cancel_exchange_form})
    
@login_required()
def delete_post(request, pk):
    post_for_deletion = Post.objects.get(pk=pk)
    post_for_deletion.delete()
    messages.success(request, "Post deleted !!")
    return redirect(exchange_noticeboard)
    
@login_required()
def create_exch_req_from_like(request, pk):
    like_for_exchange = Like.objects.get(pk=pk)
    like_for_exchange.exchange_started = True
    like_for_exchange.save()
    post_for_exchange = Post.objects.get(pk=like_for_exchange.post_liked.id)
    shift_conversion = Shift.objects.get(pk=post_for_exchange.possible_exchange_shift_id.id)
    shft_label = shift_conversion.shift_label
    new_exchange_req = ExchangeRequest(exchanging_req_officer=post_for_exchange.postee_id, exchange_req_date=post_for_exchange.possible_exchange_date, exchange_req_shift_label=shft_label, exchanging_req_officer_notes=post_for_exchange.post_content, replacing_req_officer=like_for_exchange.post_liked_by)
    new_exchange_req.save()
    #Notification to replacing officer that exchange request has been started.
    notify.send(new_exchange_req.exchanging_req_officer, recipient=new_exchange_req.replacing_req_officer, verb=" has begun an exchange with you from the noticeboard : " + str(new_exchange_req.exchange_req_date))
    messages.success(request, "You have started an exchange request with " + str(new_exchange_req.replacing_req_officer) + ".")
    
    return redirect(exchange_noticeboard)
    
@login_required()
def show_my_posts(request):
    likes = Like.objects.all()
    my_posts = Post.objects.filter(postee_id=request.user)
    len_my_posts = len(my_posts)
    my_likes = Like.objects.filter(post_liked_by=request.user)
    posts_user_liked = []
    for my_like in my_likes:
        posts_user_liked.append(my_like.post_liked.id)
    ''' Used in testing.    
    for i in posts_user_liked:
        print(i)
        print(type(i))
    '''
    list_of_liked_posts = []
    for pst in posts_user_liked:
        o = Post.objects.get(pk=pst)
        list_of_liked_posts.append(o)
    ''' Used in testing.    
    for i in list_of_liked_posts:
        print(i)
        print(type(i))
    '''   
    len_liked_posts = len(list_of_liked_posts)
    return render(request, "my_posts.html", {'my_posts': my_posts, 'list_of_liked_posts': list_of_liked_posts, 'len_my_posts': len_my_posts, 'len_liked_posts': len_liked_posts, 'likes': likes})