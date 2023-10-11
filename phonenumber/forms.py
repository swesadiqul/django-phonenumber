from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



#create forms here
class RegistrationForm(forms.Form):
    number = PhoneNumberField(widget=PhoneNumberPrefixWidget(country_choices=[('BD', 'Bangladesh'), ('IN', 'India')]))
    password = forms.CharField()
    password2 = forms.CharField()