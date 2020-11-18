{"filter":false,"title":"forms.py","tooltip":"/abscences/forms.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":38},"action":"insert","lines":["from django import forms","from .models import CertifiedSickLeave"],"id":1}],[{"start":{"row":1,"column":38},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":9,"column":71},"action":"insert","lines":["class CertifiedSickLeaveForm(forms.ModelForm):","    first_day_of_cert = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    last_day_of_cert = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    ","    class Meta:","        model = CertifiedSickLeave","        fields = ('first_day_of_cert', 'last_day_of_cert', 'csl_image')"],"id":3}],[{"start":{"row":9,"column":71},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]},{"start":{"row":10,"column":8},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":5},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":11,"column":0},"end":{"row":17,"column":47},"action":"insert","lines":["class UnCertifiedSickLeaveForm(forms.ModelForm):","    usl_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    reason_for_usl = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = UnCertifiedSickLeave","        fields = ('usl_date', 'reason_for_usl')"],"id":6}],[{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":[","],"id":7}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":[" "],"id":8},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["U"]},{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":42},"action":"remove","lines":["Un"],"id":9},{"start":{"row":1,"column":40},"end":{"row":1,"column":60},"action":"insert","lines":["UnCertifiedSickLeave"]}],[{"start":{"row":17,"column":47},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]},{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":11},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":25,"column":45},"action":"insert","lines":["class ForceMajeureForm(forms.ModelForm):","    fm_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))","    reason_for_fm = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = ForceMajeure","        fields = ('fm_date', 'reason_for_fm')"],"id":12}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"insert","lines":[","],"id":13}],[{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":1,"column":62},"end":{"row":1,"column":74},"action":"insert","lines":["ForceMajeure"],"id":15}],[{"start":{"row":25,"column":45},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]},{"start":{"row":26,"column":8},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":8},"action":"remove","lines":["    "],"id":17},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":27,"column":0},"end":{"row":46,"column":41},"action":"insert","lines":["class RejectCertifiedSickLeaveForm(forms.ModelForm):","    reason_csl_rejected = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = CertifiedSickLeave","        fields = ('reason_csl_rejected', )","        ","class RejectUnCertifiedSickLeaveForm(forms.ModelForm):","    reason_usl_rejected = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = UnCertifiedSickLeave","        fields = ('reason_usl_rejected', )","        ","class RejectForceMajeureForm(forms.ModelForm):","    reason_fm_rejected = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = ForceMajeure","        fields = ('reason_fm_rejected', )"],"id":18}]]},"ace":{"folds":[],"scrolltop":273,"scrollleft":0,"selection":{"start":{"row":46,"column":41},"end":{"row":46,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":18,"state":"start","mode":"ace/mode/python"}},"timestamp":1605725149439,"hash":"c96b3bffda446ce426cb3c070046491f6a191d5b"}