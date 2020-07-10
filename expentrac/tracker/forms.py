from django import forms
from .models import Expense
from bootstrap_modal_forms.forms import BSModalModelForm


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="Password", max_length=12, widget=forms.PasswordInput(attrs={'placeholder': '********'}))


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=20, help_text='20 characters max.', widget=forms.TextInput(attrs={'placeholder': 'sara'}))
    last_name = forms.CharField(label="Last name", max_length=30, help_text='30 characters max.', required=False, widget=forms.TextInput(attrs={'placeholder': 'khan'}))
    email = forms.EmailField(label="Email", max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'sara.email@email.com'}))
    username = forms.CharField(label="Username", max_length=15, help_text='15 characters max.', widget=forms.TextInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="Password", min_length=8, max_length=12, help_text='8 characters min, 12 characters max. There must be two numbers and two special characters each.', widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    cPassword = forms.CharField(label="Confirm Password", min_length=8, max_length=12, help_text='This must match the previous password field.', widget=forms.PasswordInput(attrs={'placeholder': '********'}))

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cPassword')

        if password and cpassword and password != cpassword:
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data


class TrackerRowForm(BSModalModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'item', 'category', 'amount', 'notes']




