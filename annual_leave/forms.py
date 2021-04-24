from django import forms
from .models import AnnualLeaveRequest, ShortTermAnnualLeaveRequest

class AnnualLeaveRequestForm(forms.ModelForm):
    leave_request_start_date = forms.DateField(label='Please select the first day of your block leave request:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    leave_request_last_date = forms.DateField(label='Please select the last day of your block leave requst:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = AnnualLeaveRequest
        fields = ('leave_request_start_date', 'leave_request_last_date')
        
class ShortTermAnnualLeaveRequestForm(forms.ModelForm):
    st_leave_date = forms.DateField(label='Please select the date for your short term leave request:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    st_leave_start_time = forms.TimeField(label='Please select the start time for your short term leave request:', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    st_leave_finish_time = forms.TimeField(label='Please select the finish time for your short term leave request:', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = ShortTermAnnualLeaveRequest
        fields = ('st_leave_date', 'st_leave_start_time', 'st_leave_finish_time')

class AnnualLeaveRequestRejectForm(forms.ModelForm):
    reason_leave_rejected = forms.CharField(label='Please outline why this annual leave request is being rejected:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = AnnualLeaveRequest
        fields = ('reason_leave_rejected',)
        
class ShortTermLeaveRequestRejectForm(forms.ModelForm):
    reason_st_leave_rejected = forms.CharField(label='Please outline why this leave request is being rejected:', required=True, widget=forms.Textarea())
    
    class Meta:
        model = ShortTermAnnualLeaveRequest
        fields = ('reason_st_leave_rejected',)