from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CertifiedSickLeaveForm, UnCertifiedSickLeaveForm, ForceMajeureForm, RejectCertifiedSickLeaveForm, RejectUnCertifiedSickLeaveForm, RejectForceMajeureForm
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure, CertifiedSickPerYear, UnCertifiedSickPerYear, ForceMajeurePerYear
from annual_leave.utils import getCurrentYear
from notifications.signals import notify
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required()
def abscences_page(request):
    '''
    This view renders the main page for the abscences section.
    '''
    user = request.user
    todays_date = datetime.date.today()
    current_yr = todays_date.year
    #Retrieve number of certified sick leave instances for current year.
    csl_for_this_year = CertifiedSickPerYear.objects.filter(yearly_csl_officer_id=user.pk).filter(csl_year=current_yr)
    len_csl_for_this_year = len(csl_for_this_year)
    if len_csl_for_this_year > 0:
        csl_for_year = CertifiedSickPerYear.objects.get(yearly_csl_officer_id=user.pk, csl_year=current_yr)
    else:
        csl_for_year = 0
    #Retrieve number of un-certified sick leave instances for current year.
    usl_for_this_year = UnCertifiedSickPerYear.objects.filter(yearly_usl_officer_id=user.pk).filter(usl_year=current_yr)
    len_usl_for_this_year = len(usl_for_this_year)
    if len_usl_for_this_year > 0:
        usl_for_year = UnCertifiedSickPerYear.objects.get(yearly_usl_officer_id=user.pk, usl_year=current_yr)
    else:
        usl_for_year = 0
    #Retrieve number of force majeure sick leave instances for current year.
    fm_for_this_year = ForceMajeurePerYear.objects.filter(yearly_fm_officer_id=user.pk).filter(fm_year=current_yr)
    len_fm_for_this_year = len(fm_for_this_year)
    if len_fm_for_this_year > 0:
        fm_for_year = ForceMajeurePerYear.objects.get(yearly_fm_officer_id=user.pk, fm_year=current_yr)
    else:
        fm_for_year = 0
        
    return render(request, "abscences_page.html", {'csl_for_year': csl_for_year, 'len_csl_for_this_year': len_csl_for_this_year, 'usl_for_year': usl_for_year, 'len_usl_for_this_year': len_usl_for_this_year, 'fm_for_year': fm_for_year, 'len_fm_for_this_year': len_fm_for_this_year})
    
@login_required()
def submit_csl(request):
    '''
    This view renders csl submission form, server side validates and creates newly submitted csl.
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
            #Check that user is not attempting to submit usl for advance dates.
            todays_date = datetime.date.today()
            if usl_form.instance.usl_date > todays_date:
                messages.error(request, "You cannot submit Un-Certified Sick Leave applications in advance of todays date.")
                return render(request, "submit_usl.html", {'usl_form': usl_form})
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
            #Check that user is not attempting to edit usl for advance dates.
            todays_date = datetime.date.today()
            if edit_usl_form.instance.usl_date > todays_date:
                messages.error(request, "You cannot submit Un-Certified Sick Leave applications in advance of todays date.")
                return render(request, "edit_usl_application.html", {'edit_usl_form': edit_usl_form})
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
            #Check that user is not attempting to submit fm for advance dates.
            todays_date = datetime.date.today()
            if fm_form.instance.fm_date > todays_date:
                messages.error(request, "You cannot submit Force Majeure applications in advance of todays date.")
                return render(request, "submit_fm.html", {'fm_form': fm_form})
            
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
    
@login_required()
def delete_fm(request, pk):
    '''
    View allows user to delete one of their own FM applications.
    '''
    fm_applic__for_deletion = ForceMajeure.objects.get(pk=pk)
    fm_applic__for_deletion.delete()
    messages.success(request, "You have successfully deleted this Force Majeure leave application.")
    return redirect('abscences_page')
    
@login_required()
def edit_fm(request, pk):
    '''
    View in combination with conditional content on view_fm_application.html allows a user to edit a previously
    submitted fm application before it is checked by a validator.
    '''
    fm_for_editing = get_object_or_404(ForceMajeure, pk=pk) if pk else None
    if request.method == "POST":
        edit_fm_form = ForceMajeureForm(request.POST, request.FILES, instance=fm_for_editing)
        if edit_fm_form.is_valid():
            #Check that user is not attempting to submit fm for advance dates.
            todays_date = datetime.date.today()
            if edit_fm_form.instance.fm_date > todays_date:
                messages.error(request, "You cannot submit Force Majeure applications in advance of todays date.")
                return render(request, "edit_fm_application.html", {'edit_fm_form': edit_fm_form})
                
            fm_for_editing = edit_fm_form.save()
            messages.success(request, 'You have successfully made changes to this force majeure application.')
            return redirect(view_fm_application, fm_for_editing.pk)
    else:
        edit_fm_form = ForceMajeureForm(instance=fm_for_editing)
    return render(request, "edit_fm_application.html", {'fm_for_editing': fm_for_editing, 'edit_fm_form': edit_fm_form})
    
@login_required()
def view_staff_sick_leave_applications(request):
    '''
    This view returns all usl, csl and fm applications made by staff for validators to check.
    '''
    staff_csl_submissions = CertifiedSickLeave.objects.select_related('csl_officer_id').filter(csl_checked_by_validator=False)
    staff_usl_submissions = UnCertifiedSickLeave.objects.select_related('usl_officer_id').filter(usl_checked_by_validator=False)
    staff_fm_submissions = ForceMajeure.objects.select_related('fm_officer_id').filter(fm_checked_by_validator=False)
    
    len_staff_csl_submissions = len(staff_csl_submissions)
    len_staff_usl_submissions = len(staff_usl_submissions)
    len_staff_fm_submissions = len(staff_fm_submissions)
    
    #Pagination for csls
    csl_pag_page_number = 1
    csl_pag_page = request.GET.get('csl_pag_page', csl_pag_page_number)
    
    csl_pag_paginator = Paginator(staff_csl_submissions, 3)
    try:
        staff_csls = csl_pag_paginator.page(csl_pag_page)
    except PageNotAnInteger:
        staff_csls = csl_pag_paginator.page(1)
    except EmptyPage:
        staff_csls = csl_pag_paginator.page(csl_pag_paginator.num_pages)
        
    #Pagination for usls
    usl_pag_page_number = 1
    usl_pag_page = request.GET.get('usl_pag_page', usl_pag_page_number)
    
    usl_pag_paginator = Paginator(staff_usl_submissions, 3)
    try:
        staff_usls = usl_pag_paginator.page(usl_pag_page)
    except PageNotAnInteger:
        staff_usls = usl_pag_paginator.page(1)
    except EmptyPage:
        staff_usls = usl_pag_paginator.page(usl_pag_paginator.num_pages)
        
    #Pagination for fms
    fm_pag_page_number = 1
    fm_pag_page = request.GET.get('fm_pag_page', fm_pag_page_number)
    
    fm_pag_paginator = Paginator(staff_fm_submissions, 3)
    try:
        staff_fms = fm_pag_paginator.page(fm_pag_page)
    except PageNotAnInteger:
        staff_fms = fm_pag_paginator.page(1)
    except EmptyPage:
        staff_fms = fm_pag_paginator.page(fm_pag_paginator.num_pages)
    
    return render(request, "staff_sick_leave_submissions.html", {'staff_csls': staff_csls, 'staff_usls': staff_usls, 'staff_fms': staff_fms, 'len_staff_csl_submissions': len_staff_csl_submissions, 'len_staff_usl_submissions': len_staff_usl_submissions, 'len_staff_fm_submissions': len_staff_fm_submissions})
    
def view_my_sick_leave(request):
    '''
    This view returns personalised list to the user showing their sick leave records. 
    '''
    officer = request.user
    my_csl = CertifiedSickLeave.objects.filter(csl_officer_id=officer.pk)
    my_usl = UnCertifiedSickLeave.objects.filter(usl_officer_id=officer.pk)
    my_fm = ForceMajeure.objects.filter(fm_officer_id=officer.pk)
    len_my_csl = len(my_csl)
    len_my_usl = len(my_usl)
    len_my_fm = len(my_fm)
    
    #Pagination for CSLs
    csl_page_number = 1
    csl_page = request.GET.get('csl_page', csl_page_number)
    
    csl_paginator = Paginator(my_csl, 3)
    try:
        my_csls = csl_paginator.page(csl_page)
    except PageNotAnInteger:
        my_csls = csl_paginator.page(1)
    except EmptyPage:
        my_csls = csl_paginator.page(csl_paginator.num_pages)
        
    #Pagination for USLs
    usl_page_number = 1
    usl_page = request.GET.get('usl_page', usl_page_number)
    
    usl_paginator = Paginator(my_usl, 2)
    try:
        my_usls = usl_paginator.page(usl_page)
    except PageNotAnInteger:
        my_usls = usl_paginator.page(1)
    except EmptyPage:
        my_usls = usl_paginator.page(usl_paginator.num_pages)
    
    #Pagination for FMs
    fm_page_number = 1
    fm_page = request.GET.get('fm_page', fm_page_number)
    
    fm_paginator = Paginator(my_fm, 2)
    try:
        my_fms = fm_paginator.page(fm_page)
    except PageNotAnInteger:
        my_fms = fm_paginator.page(1)
    except EmptyPage:
        my_fms = fm_paginator.page(fm_paginator.num_pages)
    #    
    return render(request, "my_sick_leave.html", {'my_usls': my_usls, 'my_fms': my_fms, 'len_my_csl': len_my_csl, 'len_my_usl': len_my_usl, 'len_my_fm': len_my_fm})
    
@login_required()
def accept_csl(request, pk):
    '''
    This view allows a supervisor to accept a csl application.
    '''
    csl_being_accepted = CertifiedSickLeave.objects.get(pk=pk)
    csl_being_accepted.csl_checked_by_validator = True
    csl_being_accepted.csl_accepted = True
    csl_being_accepted.save()
    current_year = getCurrentYear()
    csl_for_current_year_check = CertifiedSickPerYear.objects.filter(yearly_csl_officer_id=csl_being_accepted.csl_officer_id).filter(csl_year=current_year)
    if csl_for_current_year_check.exists():
        csl_for_current_year_check = CertifiedSickPerYear.objects.get(yearly_csl_officer_id=csl_being_accepted.csl_officer_id, csl_year=current_year)
        csl_for_current_year_check.number_csl_for_year += 1
    else:
        new_cert_sick_per_year = CertifiedSickPerYear(yearly_csl_officer_id=csl_being_accepted.csl_officer_id, csl_year=current_year, number_csl_for_year=1)
    
    #NOTIFICATION TO APPLICANT THAT CERT HAS BEEN ACCEPTED.
    notify.send(request.user, recipient=csl_being_accepted.csl_officer_id, verb=" has accepted your Certified Sick Leave application: " + str(csl_being_accepted))
    messages.success(request, "You have accepted this certified sick leave application.")
    
    return redirect('view_staff_sick_leave_applications')
    
@login_required()
def reject_csl(request, pk):
    '''
    This view allows a supervisor to reject a csl application.
    '''
    csl_being_rejected = CertifiedSickLeave.objects.get(pk=pk)
    if request.method == "POST":
        csl_reject_form = RejectCertifiedSickLeaveForm(request.POST, request.FILES, instance=csl_being_rejected)
        if csl_reject_form.is_valid():
            csl_being_rejected = csl_reject_form.save()
            csl_being_rejected.csl_checked_by_validator = True
            csl_being_rejected.csl_accepted = False
            csl_being_rejected.save()
            #NOTIFICATION TO APPLICANY THAT CERT HAS BEEN REJECTED.
            notify.send(request.user, recipient=csl_being_rejected.csl_officer_id, verb=" has rejected your Certified Sick Leave application: " + str(csl_being_rejected))
            messages.success(request, 'Cert Successfully Rejected.')
            return redirect('view_staff_sick_leave_applications')
    else:
        csl_reject_form = RejectCertifiedSickLeaveForm(instance=csl_being_rejected)
    return render(request, "reject_csl.html", {'csl_being_rejected': csl_being_rejected, 'csl_reject_form': csl_reject_form})
    
@login_required()
def accept_usl(request, pk):
    '''
    This view allows a supervisor to accept a usl application.
    '''
    usl_being_accepted = UnCertifiedSickLeave.objects.get(pk=pk)
    usl_being_accepted.usl_checked_by_validator = True
    usl_being_accepted.usl_accepted = True
    usl_being_accepted.save()
    current_year = getCurrentYear()
    usl_for_current_year_check = UnCertifiedSickPerYear.objects.filter(yearly_usl_officer_id=usl_being_accepted.usl_officer_id).filter(usl_year=current_year)
    if usl_for_current_year_check.exists():
        usl_for_current_year_check = UnCertifiedSickPerYear.objects.get(yearly_usl_officer_id=usl_being_accepted.usl_officer_id, usl_year=current_year)
        usl_for_current_year_check.number_usl_for_year += 1
        usl_for_current_year_check.save()
    else:
        new_uncert_sick_per_year = UnCertifiedSickPerYear(yearly_usl_officer_id=usl_being_accepted.usl_officer_id, usl_year=current_year, number_usl_for_year=1)
        new_uncert_sick_per_year.save()
        
    #NOTIFICATION TO APPLICANT THAT UN-CERT HAS BEEN ACCEPTED.
    notify.send(request.user, recipient=usl_being_accepted.usl_officer_id, verb=" has accepted your Un-Certified Sick Leave application: " + str(usl_being_accepted))
    messages.success(request, "You have accepted this uncertified sick leave application.")
    
    return redirect('view_staff_sick_leave_applications')
    
@login_required()
def reject_usl(request, pk):
    '''
    This view allows a supervisor to reject a usl application.
    '''
    usl_being_rejected = UnCertifiedSickLeave.objects.get(pk=pk)
    if request.method == "POST":
        usl_reject_form = RejectUnCertifiedSickLeaveForm(request.POST, request.FILES, instance=usl_being_rejected)
        if usl_reject_form.is_valid():
            usl_being_rejected = usl_reject_form.save()
            usl_being_rejected.usl_checked_by_validator = True
            usl_being_rejected.usl_accepted = False
            usl_being_rejected.save()
            #NOTIFUCATION TO APPLICANY THAT UN-CERT HAS BEEN REJECTED.
            notify.send(request.user, recipient=usl_being_rejected.usl_officer_id, verb=" has rejected your Un-Certified Sick Leave application: " + str(usl_being_rejected))
            messages.success(request, 'USL Application Rejected.')
            return redirect('view_staff_sick_leave_applications')
    else:
        usl_reject_form = RejectUnCertifiedSickLeaveForm(instance=usl_being_rejected)
    return render(request, "reject_usl.html", {'usl_being_rejected': usl_being_rejected, 'usl_reject_form': usl_reject_form})
    
@login_required()
def accept_fm(request, pk):
    '''
    This view allows a supervisor to accept a fm application.
    '''
    fm_being_accepted = ForceMajeure.objects.get(pk=pk)
    fm_being_accepted.fm_checked_by_validator = True
    fm_being_accepted.fm_accepted = True
    fm_being_accepted.save()
    current_year = getCurrentYear()
    fm_for_current_year_check = ForceMajeurePerYear.objects.filter(yearly_fm_officer_id=fm_being_accepted.fm_officer_id).filter(fm_year=current_year)
    if fm_for_current_year_check.exists():
        fm_for_current_year_check = ForceMajeurePerYear.objects.get(yearly_fm_officer_id=fm_being_accepted.fm_officer_id, fm_year=current_year)
        fm_for_current_year_check.number_fm_for_year += 1
    else:
        new_fm_for_year = ForceMajeurePerYear(yearly_fm_officer_id=fm_being_accepted.fm_officer_id, fm_year=current_year, number_fm_for_year=1)
    #NOTIFICATION TO APPLICANT THAT FM ACCEPTED.
    notify.send(request.user, recipient=fm_being_accepted.fm_officer_id, verb=" has accepted your Force Majeure application: " + str(fm_being_accepted))
    messages.success(request, "Force Majeure application accepted.")
    return redirect('view_staff_sick_leave_applications')
    
@login_required()
def reject_fm(request, pk):
    '''
    This view allows a supervisor to reject a fm application.
    '''
    fm_being_rejected = ForceMajeure.objects.get(pk=pk)
    if request.method == "POST":
        fm_reject_form = RejectForceMajeureForm(request.POST, request.FILES, instance=fm_being_rejected)
        if fm_reject_form.is_valid():
            fm_being_rejected = fm_reject_form.save()
            fm_being_rejected.fm_checked_by_validator = True
            fm_being_rejected.fm_accepted = False
            fm_being_rejected.save()
            #NOTIFICATION TO APPLICANT THAT UN-CERT HAS BEEN REJECTED.
            notify.send(request.user, recipient=fm_being_rejected.fm_officer_id, verb=" has rejected your Force Majeure application: " + str(fm_being_rejected))
            messages.success(request, 'Force Majeure Application Rejected.')
            return redirect('view_staff_sick_leave_applications')
    else:
        fm_reject_form = RejectForceMajeureForm(instance=fm_being_rejected)
    return render(request, "reject_fm.html", {'fm_being_rejected': fm_being_rejected, 'fm_reject_form': fm_reject_form})