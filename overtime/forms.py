from django import forms
from django.db.models import Q
from .models import AvailabilitySheet, NonScheduledOvertimeRequest, AllowancesRequest, ShortTermAvailabilty
from .utils import getNextQtr, getCurrentQtr, getQtrDateIn
from clocking.models import Roster, Shift
from account.models import Account
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
import datetime as dt
from datetime import datetime

class AvailabilitySheetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AvailabilitySheetForm, self).__init__(*args, **kwargs)
        user_as_simpleLazyObject = get_current_user()
        user = Account.objects.get(pk=user_as_simpleLazyObject.id)
        #print(user)
        next_qtr = getNextQtr()
        #print(next_qtr)
        monday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=2)
        monday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in monday_query]
        self.fields['mon_one'] = forms.ChoiceField(widget=forms.Select, choices=monday_query_choices)
        self.fields['mon_two'] = forms.ChoiceField(widget=forms.Select, choices=monday_query_choices)
        tuesday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=3)
        tuesday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in tuesday_query]
        self.fields['tue_one'] = forms.ChoiceField(widget=forms.Select, choices=tuesday_query_choices)
        self.fields['tue_two'] = forms.ChoiceField(widget=forms.Select, choices=tuesday_query_choices)
        wednesday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=4)
        wednesday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in wednesday_query]
        self.fields['wed_one'] = forms.ChoiceField(widget=forms.Select, choices=wednesday_query_choices)
        self.fields['wed_two'] = forms.ChoiceField(widget=forms.Select, choices=wednesday_query_choices)
        thursday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=5)
        thursday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in thursday_query]
        self.fields['thurs_one'] = forms.ChoiceField(widget=forms.Select, choices=thursday_query_choices)
        self.fields['thurs_two'] = forms.ChoiceField(widget=forms.Select, choices=thursday_query_choices)
        friday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=6)
        friday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in friday_query]
        self.fields['fri_one'] = forms.ChoiceField(widget=forms.Select, choices=friday_query_choices)
        self.fields['fri_two'] = forms.ChoiceField(widget=forms.Select, choices=friday_query_choices)
        saturday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=7)
        saturday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in saturday_query]
        self.fields['sat_one'] = forms.ChoiceField(widget=forms.Select, choices=saturday_query_choices)
        self.fields['sat_two'] = forms.ChoiceField(widget=forms.Select, choices=saturday_query_choices)
        sunday_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gte=next_qtr.qtr_start_date).filter(roster_shift_date__lte=next_qtr.qtr_end_date).filter(roster_shift_date__week_day=1)
        sunday_query_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in sunday_query]
        self.fields['sun_one'] = forms.ChoiceField(widget=forms.Select, choices=sunday_query_choices)
        self.fields['sun_two'] = forms.ChoiceField(widget=forms.Select, choices=sunday_query_choices)
        
    class Meta:
        model = AvailabilitySheet
        fields = ('mon_one', 'mon_two', 'tue_one', 'tue_two', 'wed_one', 'wed_two', 'thurs_one', 'thurs_two', 'fri_one', 'fri_two', 'sat_one', 'sat_two', 'sun_one', 'sun_two')
        

class NonScheduledOvertimeRequestForm(forms.ModelForm):
    nsot_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    nsot_start_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    nsot_end_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    nsot_task = forms.CharField(required=True, widget=forms.Textarea())
    directed_by = forms.ModelChoiceField(widget=forms.Select, queryset=Account.objects.filter(is_staff=True))
    
    class Meta:
        model = NonScheduledOvertimeRequest
        fields = ('nsot_date', 'nsot_start_time', 'nsot_end_time', 'nsot_task', 'directed_by')
        
        
class AllowancesRequestForm(forms.ModelForm):
    allow_req_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    allow_req_task = forms.CharField(required=True, widget=forms.Textarea())
    claiming_breakfast_allowance = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    claiming_dinner_allowance = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    claiming_tea_allowance = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    claiming_plain_clothes_allowance = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    claiming_food_for_prisoner_expense = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    food_for_prisoner_amount = forms.FloatField(required=False, widget=forms.NumberInput)
    
    class Meta:
        model = AllowancesRequest
        fields = ('allow_req_date', 'allow_req_task', 'claiming_breakfast_allowance', 'claiming_dinner_allowance', 'claiming_tea_allowance', 'claiming_plain_clothes_allowance', 'claiming_food_for_prisoner_expense', 'food_for_prisoner_amount', 'receipt_for_prisoner_food',)
        

class RejectAllowanceRequestForm(forms.ModelForm):
    reason_allowance_req_rejected = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = AllowancesRequest
        fields = ('reason_allowance_req_rejected', )
        
        
class RejectNSOTForm(forms.ModelForm):
    reason_nsot_rejected = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = NonScheduledOvertimeRequest
        fields = ('reason_nsot_rejected', )
        
        
class AssignOvertimeDateForm(forms.Form):
    date_for_assignment = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    

class AssignRecallStaffForm(forms.Form):
    def __init__(self, *args, **kwargs):
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        selected_dat = initial_arguments.get('selected_date', None)
        selected_date_1 = datetime.strptime(selected_dat, "%Y-%m-%d")
        selected_date = dt.date(selected_date_1.year, selected_date_1.month, selected_date_1.day)
        updated_initial['selected_date'] = selected_date
        kwargs.update(initial=updated_initial)
        
        super(AssignRecallStaffForm, self).__init__(*args, **kwargs)
        qtr = getQtrDateIn(selected_date)
        no_staff_available_for_selected_date = False
        
        self.fields['selected_date'] = forms.DateField(disabled=True)
        
        if selected_date.strftime("%A") == "Monday":
            mon_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(mon_one__contains=selected_date) | Q(mon_two__contains=selected_date))
            length_mon_query = len(mon_query)
            if length_mon_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                mon_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in mon_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=mon_off_query_choices)
        elif selected_date.strftime("%A") == "Tuesday":
            tue_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(tue_one__contains=selected_date) | Q(tue_two__contains=selected_date))
            length_tue_query = len(tue_query)
            if length_tue_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                tue_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in tue_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=tue_off_query_choices)
        elif selected_date.strftime("%A") == "Wednesday":
            wed_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(wed_one__contains=selected_date) | Q(wed_two__contains=selected_date))
            length_wed_query = len(wed_query)
            if length_wed_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                wed_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in wed_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=wed_off_query_choices)
        elif selected_date.strftime("%A") == "Thursday":
            thurs_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(thurs_one__contains=selected_date) | Q(thurs_two__contains=selected_date))
            length_thurs_query = len(thurs_query)
            if length_thurs_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                thurs_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in thurs_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=thurs_off_query_choices)
        elif selected_date.strftime("%A") == "Friday":
            fri_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(fri_one__contains=selected_date) | Q(fri_two__contains=selected_date))
            length_fri_query = len(fri_query)
            if length_fri_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                fri_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in fri_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=fri_off_query_choices)
        elif selected_date.strftime("%A") == "Saturday":
            sat_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(sat_one__contains=selected_date) | Q(sat_two__contains=selected_date))
            length_sat_query = len(sat_query)
            if length_sat_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                sat_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in sat_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=sat_off_query_choices)    
        elif selected_date.strftime("%A") == "Sunday":
            sun_query = AvailabilitySheet.objects.filter(avail_sheet_qtr_id=qtr).filter(Q(sun_one__contains=selected_date) | Q(sun_two__contains=selected_date))
            length_sun_query = len(sun_query)
            if length_sun_query == 0:
                no_staff_available_for_selected_date = True
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, disabled=True, help_text="No staff have made themselves available for " + str(selected_date) + ".")
            else:
                sun_off_query_choices = [('', 'Select available staff member')] + [(id.avail_sheet_off_id, id.avail_sheet_off_id) for id in sun_query]
                self.fields['officers_available'] = forms.ChoiceField(widget=forms.Select, choices=sun_off_query_choices)
        
        if no_staff_available_for_selected_date == True:
            self.fields['assign_shift'] = forms.ChoiceField(widget=forms.Select, disabled=True)
        else:
            self.fields['assign_shift'] = forms.ModelChoiceField(widget=forms.Select, queryset=Shift.objects.all())
        
        
class AssignRequireStaffForm(forms.Form):
   def __init__(self, *args, **kwargs):
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        selected_date_as_string = initial_arguments.get('selected_require_date', None)
        selected_date_as_dt_obj = datetime.strptime(selected_date_as_string, "%Y-%m-%d")
        selected_require_date = dt.date(selected_date_as_dt_obj.year, selected_date_as_dt_obj.month, selected_date_as_dt_obj.day)
        updated_initial['selected_require_date'] = selected_require_date
        kwargs.update(initial=updated_initial)
        super(AssignRequireStaffForm, self).__init__(*args, **kwargs)
        
        self.fields['selected_require_date'] = forms.DateField(disabled=True)
        
        officers_that_can_be_required = Roster.objects.filter(roster_shift_date__contains=selected_require_date).filter(roster_due_on=False)
        off_to_require_query_choices = [('', 'select staff member to require')] + [(id.roster_officer_id, id.roster_officer_id) for id in officers_that_can_be_required]
        self.fields['officers_for_require'] = forms.ChoiceField(widget=forms.Select, choices=off_to_require_query_choices)
        
        self.fields['assign_require_shift'] = forms.ModelChoiceField(widget=forms.Select, queryset=Shift.objects.all())
        
class ShortTermAvailabilityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShortTermAvailabilityForm, self).__init__(*args, **kwargs)
        user_as_simpleLazyObject = get_current_user()
        user = Account.objects.get(pk=user_as_simpleLazyObject.id)
        todays_date = dt.date.today()
        thirteen_day_delta = dt.timedelta(days=13)
        short_term_window_end = todays_date + thirteen_day_delta
        
        short_term_days_query = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=False).filter(roster_shift_date__gt=todays_date).filter(roster_shift_date__lte=short_term_window_end)
        short_term_availability_choices = [('', 'select date')] + [(id.roster_shift_date.strftime("%Y-%m-%d"), id.roster_shift_date.strftime("%Y-%m-%d")) for id in short_term_days_query]
        self.fields['st_availability_date'] = forms.ChoiceField(widget=forms.Select, choices=short_term_availability_choices)
        
    class Meta:
        model = ShortTermAvailabilty
        fields = ('st_availability_date', )
        
class AssignShortTermOTDateForm(forms.Form):
    date_for_st_assignment = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))