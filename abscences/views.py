from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CertifiedSickLeaveForm, UnCertifiedSickLeaveForm, ForceMajeureForm, RejectCertifiedSickLeaveForm, RejectUnCertifiedSickLeaveForm, RejectForceMajeureForm
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure, CertifiedSickPerYear, UnCertifiedSickPerYear, ForceMajeurePerYear
from annual_leave.utils import getCurrentYear
from notifications.signals import notify

# Create your views here.
@login_required()
def abscences_page(request):
    '''
    This view renders the main page for the abscences section.
    '''
    return render(request, "abscences_page.html")
    
@login_required()
def submit_csl(request):
    '''
    This view renders, server side validates and creates newly submitted csl.
    '''
    if request.method == "POST":
        csl_form = CertifiedSickLeaveForm(request.POST, request.FILES)
        if csl_form.is_valid():
            csl_form.instance.csl_officer_id = request.user
            if csl_form.instance.first_day_of_cert > csl_form.instance.last_day_of_cert:
                messages.error(request, "The start date for the cert must be before the last date.")
                return render(request, "submit_csl.html", {'csl_form': csl_form})
            else:
                csl_application = csl_form.save()
                messages.success(request, 'You have successfully submitted a certified sick leave application.')
                return redirect(view_csl_application, csl_application.pk)
    else:
        csl_form = CertifiedSickLeaveForm()
    return render(request, "submit_csl.html", {'csl_form': csl_form})
    
@login_required()
def view_csl_application(request, pk):
    '''
    This view displays a single csl application.
    '''
    csl_application = get_object_or_404(CertifiedSickLeave, pk=pk)
    csl_application.save()
    return render(request, "view_csl_application.html", {'csl_application': csl_application})
    
@login_required()
def delete_csl(request, pk):
    '''
    This view allows user to delete a csl application.
    '''
    csl_applic_for_deletion = CertifiedSickLeave.objects.get(pk=pk)
    csl_applic_for_deletion.delete()
    messages.success(request, "You have successfully deleted this certified sick leave application.")
    return redirect('abscences_page')
    
@login_required()
def edit_csl(request, pk):
    '''
    This view allows the user edit a previously submitted csl application.
    '''
    csl_for_editing = get_object_or_404(CertifiedSickLeave, pk=pk) if pk else None
    if request.method == "POST":
        edit_csl_form = CertifiedSickLeaveForm(request.POST, request.FILES, instance=csl_for_editing)
        if edit_csl_form.is_valid():
            csl_for_editing = edit_csl_form.save()
            messages.success(request, 'You have successfully made changes to this certified sick leave application.')
            return redirect(view_csl_application, csl_for_editing.pk)
    else:
        edit_csl_form = CertifiedSickLeaveForm(instance=csl_for_editing)
    return render(request, "edit_csl_application.html", {'csl_for_editing': csl_for_editing, 'edit_csl_form': edit_csl_form})