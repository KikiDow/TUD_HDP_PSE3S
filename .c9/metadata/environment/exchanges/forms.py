{"filter":false,"title":"forms.py","tooltip":"/exchanges/forms.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":4,"column":34},"action":"insert","lines":["from django import forms","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth import authenticate","","from account.models import Account"],"id":1}],[{"start":{"row":4,"column":34},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":4,"column":34},"action":"remove","lines":["from django import forms","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth import authenticate","","from account.models import Account"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":77,"column":64},"action":"insert","lines":["from django import forms","from django_currentuser.middleware import get_current_user, get_current_authenticated_user","from account.models import Account","from clocking.models import Roster","from .models import Post, ExchangeRequest","import datetime","","class PostForm(forms.ModelForm):","    def __init__(self, *args, **kwargs):","        super(PostForm, self).__init__(*args, **kwargs)","        user_as_simpleLazyObject = get_current_user()","        user = Account.objects.get(pk=user_as_simpleLazyObject.id)","        todays_date = datetime.date.today()","        exchangers_roster = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=True).filter(roster_shift_date__gt=todays_date)","        exchangers_roster_choices = [('', 'select date')] + [(id.roster_shift_date.strftime(\"%Y-%m-%d\"), id.roster_shift_date.strftime(\"%Y-%m-%d\")) for id in exchangers_roster]","        self.fields['possible_exchange_date'] = forms.ChoiceField(widget=forms.Select, choices=exchangers_roster_choices)","        self.fields['post_content'] = forms.CharField(required=False, widget=forms.Textarea())","        ","    class Meta:","        model = Post","        fields = ('possible_exchange_date', 'post_content')","        ","class SubmitExchangeRequestExchangingOfficerForm(forms.ModelForm):","    def __init__(self, *args, **kwargs):","        super(SubmitExchangeRequestExchangingOfficerForm, self).__init__(*args, **kwargs)","        user_as_simpleLazyObject = get_current_user()","        user = Account.objects.get(pk=user_as_simpleLazyObject.id)","        user_roster_side = user.roster_side","        todays_date = datetime.date.today()","        exchangers_roster = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=True).filter(roster_shift_date__gt=todays_date)","        exchangers_roster_choices = [('', 'select date')] + [(id.roster_shift_date.strftime(\"%Y-%m-%d\"), id.roster_shift_date.strftime(\"%Y-%m-%d\")) for id in exchangers_roster]","        self.fields['exchange_req_date'] = forms.ChoiceField(widget=forms.Select, choices=exchangers_roster_choices)","        if user_roster_side == \"A\":","            self.fields['replacing_req_officer'] = forms.ModelChoiceField(widget=forms.Select, queryset=Account.objects.filter(roster_side=\"B\"))","        else:","            self.fields['replacing_req_officer'] = forms.ModelChoiceField(widget=forms.Select, queryset=Account.objects.filter(roster_side=\"A\"))","            ","        self.fields['exchanging_req_officer_notes'] = forms.CharField(required=False, widget=forms.Textarea())","        ","    class Meta:","        model = ExchangeRequest","        fields = ('exchange_req_date', 'replacing_req_officer', 'exchanging_req_officer_notes')","        ","class SubmitExchangeRequestReplacingOfficerForm(forms.ModelForm):","    #NEED INITIAL VALUES FOR E.O. AND R.O. IDENTITY","    def __init__(self, *args, **kwargs):","        super(SubmitExchangeRequestReplacingOfficerForm, self).__init__(*args, **kwargs)","        #initial_arguments = kwargs.get('initial', None)","        user_as_simpleLazyObject = get_current_user()","        user = Account.objects.get(pk=user_as_simpleLazyObject.id)","        user_roster_side = user.roster_side","        todays_date = datetime.date.today()","        #self.fields exchange officer, date, shift, notes, replacing officer?? <all disabled>","        replacers_roster = Roster.objects.filter(roster_officer_id=user).filter(roster_due_on=True).filter(roster_shift_date__gt=todays_date)","        replacers_roster_choices = [('', 'select date')] + [(id.roster_shift_date.strftime(\"%Y-%m-%d\"), id.roster_shift_date.strftime(\"%Y-%m-%d\")) for id in replacers_roster]","        self.fields['replacing_req_date'] = forms.ChoiceField(widget=forms.Select, choices=replacers_roster_choices)","        self.fields['replacing_req_officer_notes'] = forms.CharField(required=False, widget=forms.Textarea())","        self.fields['ro_proceed_with_swap'] = forms.BooleanField(required=False, widget=forms.CheckboxInput)","        ","    class Meta:","        model = ExchangeRequest","        #fields = ('exchanging_req_officer', 'exchange_req_date', 'exchange_req_shift_label', 'exchanging_req_officer_notes', 'replacing_req_officer', 'replacing_req_date', 'replacing_req_officer_notes', 'ro_proceed_with_swap')","        fields = ('replacing_req_date', 'replacing_req_officer_notes', 'ro_proceed_with_swap')","        ","class SubmitExchangeRequestExchangingOfficerCheckForm(forms.ModelForm):","    eo_proceed_with_swap = forms.BooleanField(required=False, widget=forms.CheckboxInput)","        ","    class Meta:","        model = ExchangeRequest","        fields = ('eo_proceed_with_swap', )","        ","class CancelExchangeRequestForm(forms.ModelForm):","    swap_cancelled = forms.BooleanField(required=False, widget=forms.CheckboxInput)","    reason_exchange_cancelled = forms.CharField(required=True, widget=forms.Textarea())","    ","    class Meta:","        model = ExchangeRequest","        fields = ('swap_cancelled', 'reason_exchange_cancelled')"],"id":4}]]},"ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"timestamp":1605953728222,"hash":"475b98eabd9ac9e447fde4440e18b2eb0f7aa4c4"}