from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CertifiedSickLeaveForm, UnCertifiedSickLeaveForm, ForceMajeureForm, RejectCertifiedSickLeaveForm, RejectUnCertifiedSickLeaveForm, RejectForceMajeureForm
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure, CertifiedSickPerYear, UnCertifiedSickPerYear, ForceMajeurePerYear
#from annual_leave.utils import getCurrentYear
from notifications.signals import notify

# Create your views here.
@login_required()
def abscences_page(request):
    return render(request, "abscences_page.html")