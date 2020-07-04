from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="Password", max_length=12, widget=forms.TextInput(attrs={'placeholder': '********'}))


class SignUp(forms.Form):
    first_name = forms.CharField(label="First name", max_length=20, widget=forms.TextInput(attrs={'placeholder': 'sara'}))
    last_name = forms.CharField(label="Last name", max_length=30, widget=forms.TextInput(attrs={'placeholder': 'khan'}))
    email = forms.EmailField(label="Email", max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'sara.email@email.com'}))
    username = forms.CharField(label="Username", max_length=15, widget=forms.EmailInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="First name", max_length=8, widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    cPassword = forms.CharField(label="First name", max_length=8, widget=forms.PasswordInput(attrs={'placeholder': '********'}))




