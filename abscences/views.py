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
    
#USL
@login_required()
def submit_usl(request):
    '''
    This view allows the user to submit and create a usl application.
    '''
    if request.method == "POST":
        usl_form = UnCertifiedSickLeaveForm(request.POST, request.FILES)
        if usl_form.is_valid():
            usl_form.instance.usl_officer_id = request.user
            usl_application = usl_form.save()
            messages.success(request, 'You have successfully submitted an uncertified sick leave application.')
            return redirect(view_usl_application, usl_application.pk)
    else:
        usl_form = UnCertifiedSickLeaveForm()
    return render(request, "submit_usl.html", {'usl_form': usl_form})
    
@login_required()
def view_usl_application(request, pk):
    '''
    This view allows the user to view a single usl application and its status.
    '''
    usl_application = get_object_or_404(UnCertifiedSickLeave, pk=pk)
    usl_application.save()
    return render(request, "view_usl_application.html", {'usl_application': usl_application})
    
@login_required()
def delete_usl(request, pk):
    '''
    View to delete usl application.
    '''
    usl_applic_for_deletion = UnCertifiedSickLeave.objects.get(pk=pk)
    usl_applic_for_deletion.delete()
    messages.success(request, "You have successfully deleted this uncertified sick leave application.")
    return redirect('abscences_page')
    
@login_required()
def edit_usl(request, pk):
    '''
    This view allows a user to edit a usl application prior to being checked by a validator.
    '''
    usl_for_editing = get_object_or_404(UnCertifiedSickLeave, pk=pk) if pk else None
    if request.method == "POST":
        edit_usl_form = UnCertifiedSickLeaveForm(request.POST, request.FILES, instance=usl_for_editing)
        if edit_usl_form.is_valid():
            usl_for_editing = edit_usl_form.save()
            messages.success(request, 'You have successfully made changes to this uncertified sick leave application.')
            return redirect(view_usl_application, usl_for_editing.pk)
    else:
        edit_usl_form = UnCertifiedSickLeaveForm(instance=usl_for_editing)
    return render(request, "edit_usl_application.html", {'usl_for_editing': usl_for_editing, 'edit_usl_form': edit_usl_form})
    
#FM - SUBMIT, VIEW, EDIT & DELETE.
@login_required()
def submit_fm(request):
    '''
    This view allows a user to submit a FM application.
    '''
    if request.method == "POST":
        fm_form = ForceMajeureForm(request.POST, request.FILES)
        if fm_form.is_valid():
            fm_form.instance.fm_officer_id = request.user
            fm_application = fm_form.save()
            messages.success(request, 'You have successfully submitted a Force Majeure application.')
            return redirect(view_fm_application, fm_application.pk)
    else:
        fm_form = ForceMajeureForm()
    return render(request, "submit_fm.html", {'fm_form': fm_form})
    
@login_required()
def view_fm_application(request, pk):
    '''
    This view allows the user to view a FM application.
    '''
    fm_application = get_object_or_404(ForceMajeure, pk=pk)
    fm_application.save()
    return render(request, "view_fm_application.html", {'fm_application': fm_application})