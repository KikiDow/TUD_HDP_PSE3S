from django import forms
from .models import PersonalDetails, ManualClocking

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('address_1', 'address_2', 'eircode', 'county', 'contact_number', 'personal_email', 'emergency_contact', 'relationship_to_emergency_contact', 'emergency_contact_number')

class ManualClockingForm(forms.ModelForm):
    
    clocking_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    clocking_in_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    lunch_out_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    lunch_in_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    clocking_out_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    reason_for_missed_clocking = forms.CharField(required=True, widget=forms.Textarea())

    class Meta:
        model = ManualClocking
        fields = ('clocking_date', 'clocking_in_time', 'lunch_out_time', 'lunch_in_time', 'clocking_out_time', 'reason_for_missed_clocking')
        
class RejectManualClockingForm(forms.ModelForm):
    reason_manual_clock_rejected = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = ManualClocking
        fields = ('reason_manual_clock_rejected',)