from django import forms
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure

class CertifiedSickLeaveForm(forms.ModelForm):
    first_day_of_cert = forms.DateField(label='Please select the first day covered by your medical cert:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    last_day_of_cert = forms.DateField(label='Please select the last day covered by your medical cert:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = CertifiedSickLeave
        fields = ('first_day_of_cert', 'last_day_of_cert', 'csl_image')
        
class UnCertifiedSickLeaveForm(forms.ModelForm):
    usl_date = forms.DateField(label='Please select the date of your U.S.L.:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    reason_for_usl = forms.CharField(label='Please outline the reason why you had to take a U.S.L.:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = UnCertifiedSickLeave
        fields = ('usl_date', 'reason_for_usl')
        
class ForceMajeureForm(forms.ModelForm):
    fm_date = forms.DateField(label='Please select the date of your Force Majeure:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    reason_for_fm = forms.CharField(label='Please outline the reason why you had to avail of Force Majeure leave:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = ForceMajeure
        fields = ('fm_date', 'reason_for_fm')
        
class RejectCertifiedSickLeaveForm(forms.ModelForm):
    reason_csl_rejected = forms.CharField(label='Please outline why this Certified Sick Leave application is being rejected:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = CertifiedSickLeave
        fields = ('reason_csl_rejected', )
        
class RejectUnCertifiedSickLeaveForm(forms.ModelForm):
    reason_usl_rejected = forms.CharField(label='Please outline why this Un-Certified Sick Leave application is being rejected:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = UnCertifiedSickLeave
        fields = ('reason_usl_rejected', )
        
class RejectForceMajeureForm(forms.ModelForm):
    reason_fm_rejected = forms.CharField(label='Please outline why this Force Majeure application is being rejected:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = ForceMajeure
        fields = ('reason_fm_rejected', )