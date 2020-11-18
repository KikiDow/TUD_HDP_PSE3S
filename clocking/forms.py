from django import forms
from .models import PersonalDetails

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('address_1', 'address_2', 'eircode', 'county', 'contact_number', 'personal_email', 'emergency_contact', 'relationship_to_emergency_contact', 'emergency_contact_number')
        