from django import forms
from .models import PersonalDetails, ManualClocking

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('address_1', 'address_2', 'eircode', 'county', 'contact_number', 'personal_email', 'emergency_contact', 'relationship_to_emergency_contact', 'emergency_contact_number')
        labels = {
            "address_1": "Address Line 1: ",
            "address_2": "Address Line 2: ",
            "eircode": "Eircode: ",
            "county": "County",
            "contact_number": "Your Contact Number: ",
            "personal_email": "Your Personal Email: ",
            "emergency_contact": "Emergency Contact Name: ",
            "relationship_to_emergency_contact": "Your relationship to your emergency contact: ",
            "emergency_contact_number": "Emergency Contact Telephone Number: ",
        }

class ManualClockingForm(forms.ModelForm):
    
    clocking_date = forms.DateField(label="Please select the date:", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    clocking_in_time = forms.TimeField(label="Please select a clocking-in time:", required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    lunch_out_time = forms.TimeField(label="Please select a lunch-out clocking time:", required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    lunch_in_time = forms.TimeField(label="Please select a lunch-in clocking time:",required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    clocking_out_time = forms.TimeField(label="Please select a clocking-out time:", required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    reason_for_missed_clocking = forms.CharField(label="Please outline why you were unable to clock on this date:", required=True, widget=forms.Textarea())

    class Meta:
        model = ManualClocking
        fields = ('clocking_date', 'clocking_in_time', 'lunch_out_time', 'lunch_in_time', 'clocking_out_time', 'reason_for_missed_clocking')
        
class RejectManualClockingForm(forms.ModelForm):
    reason_manual_clock_rejected = forms.CharField(label="Please outline why this manual clocking application is being rejected:", required=True, widget=forms.Textarea())
    
    class Meta:
        model = ManualClocking
        fields = ('reason_manual_clock_rejected',)