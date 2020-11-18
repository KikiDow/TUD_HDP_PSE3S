from django import forms
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure

class CertifiedSickLeaveForm(forms.ModelForm):
    first_day_of_cert = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    last_day_of_cert = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = CertifiedSickLeave
        fields = ('first_day_of_cert', 'last_day_of_cert', 'csl_image')
        
class UnCertifiedSickLeaveForm(forms.ModelForm):
    usl_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    reason_for_usl = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = UnCertifiedSickLeave
        fields = ('usl_date', 'reason_for_usl')
        
class ForceMajeureForm(forms.ModelForm):
    fm_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    reason_for_fm = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = ForceMajeure
        fields = ('fm_date', 'reason_for_fm')
        
class RejectCertifiedSickLeaveForm(forms.ModelForm):
    reason_csl_rejected = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = CertifiedSickLeave
        fields = ('reason_csl_rejected', )
        
class RejectUnCertifiedSickLeaveForm(forms.ModelForm):
    reason_usl_rejected = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = UnCertifiedSickLeave
        fields = ('reason_usl_rejected', )
        
class RejectForceMajeureForm(forms.ModelForm):
    reason_fm_rejected = forms.CharField(required=True, widget=forms.Textarea())
    
    class Meta:
        model = ForceMajeure
        fields = ('reason_fm_rejected', )