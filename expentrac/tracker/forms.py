from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15, help_text='15 characters max.', widget=forms.TextInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="Password", max_length=12, help_text='8 characters min, 12 characters max. There must be two numbers and two special characters each.', widget=forms.PasswordInput(attrs={'placeholder': '********'}))


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=20, widget=forms.TextInput(attrs={'placeholder': 'sara'}))
    last_name = forms.CharField(label="Last name", max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'khan'}))
    email = forms.EmailField(label="Email", max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'sara.email@email.com'}))
    username = forms.CharField(label="Username", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="Password", max_length=8, widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    cPassword = forms.CharField(label="Confirm Password", max_length=8, widget=forms.PasswordInput(attrs={'placeholder': '********'}))




