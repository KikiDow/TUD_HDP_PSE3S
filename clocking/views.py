from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
#from .models import Quarter, Shift, RosterSideA, RosterSideB, Roster
from django.contrib import messages
from.utils import findRosterStartPoint, rosterPointerCheck
from account.models import Account
# Create your views here.

def landing_page(request):
    '''
    A view that renders the landing page of the application.
    '''
    return render(request, "landing_page.html")
