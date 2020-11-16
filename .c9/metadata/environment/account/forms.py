{"filter":false,"title":"forms.py","tooltip":"/account/forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":29,"column":48},"action":"insert","lines":["from django import forms","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth import authenticate","","from account.models import Account","","class RegistrationForm(UserCreationForm):","    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')","    is_staff = forms.BooleanField(required=False, widget=forms.CheckboxInput)","","    class Meta:","        model = Account","        fields = ('email', 'username', 'firstname', 'lastname', 'is_staff', 'roster_side', 'password1', 'password2')","","","       ","class AccountAuthenticationForm(forms.ModelForm):","","\tpassword = forms.CharField(label='Password', widget=forms.PasswordInput)","","\tclass Meta:","\t\tmodel = Account","\t\tfields = ('email', 'password')","","\tdef clean(self):","\t\tif self.is_valid():","\t\t\temail = self.cleaned_data['email']","\t\t\tpassword = self.cleaned_data['password']","\t\t\tif not authenticate(email=email, password=password):","\t\t\t\traise forms.ValidationError(\"Invalid login\")"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":7},"end":{"row":15,"column":7},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605539947670,"hash":"1a3665ff9a34990acc14885bcc126b9a864c9185"}