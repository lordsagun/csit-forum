from django.forms import ModelForm
from .models import Myuser
from django import forms

class SignupForm(ModelForm):
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    re_password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.EmailInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label})
    class Meta:
        model = Myuser
        exclude = ['points','is_active','is_admin','last_login']
