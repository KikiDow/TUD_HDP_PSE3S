{"filter":false,"title":"forms.py","tooltip":"/annual_leave/forms.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":33,"column":46},"action":"insert","lines":["from django import forms","from .models import AnnualLeaveRequest, ShortTermAnnualLeaveRequest","","class AnnualLeaveRequestForm(forms.ModelForm):","    leave_request_start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    leave_request_last_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    ","    class Meta:","        model = AnnualLeaveRequest","        fields = ('leave_request_start_date', 'leave_request_last_date')","        ","class ShortTermAnnualLeaveRequestForm(forms.ModelForm):","    st_leave_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    st_leave_start_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))","    st_leave_finish_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))","    #st_leave_amount = forms.IntegerField(required=True, widget=forms.NumberInput())","    ","    class Meta:","        model = ShortTermAnnualLeaveRequest","        fields = ('st_leave_date', 'st_leave_start_time', 'st_leave_finish_time')","","class AnnualLeaveRequestRejectForm(forms.ModelForm):","    reason_leave_rejected = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = AnnualLeaveRequest","        fields = ('reason_leave_rejected',)","        ","class ShortTermLeaveRequestRejectForm(forms.ModelForm):","    reason_st_leave_rejected = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = ShortTermAnnualLeaveRequest","        fields = ('reason_st_leave_rejected',)"],"id":1}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":84},"action":"remove","lines":["#st_leave_amount = forms.IntegerField(required=True, widget=forms.NumberInput())"],"id":2},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":105},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":105},"end":{"row":14,"column":105},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605728499165,"hash":"89c3f78ab5d73fff303e6da6351d3dc5b6b10840"}