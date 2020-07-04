from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'sarakhan'}))
    password = forms.CharField(label="Password", max_length=12, widget=forms.TextInput(attrs={'placeholder': '********'}))

class SignUp(forms.Form):
    fname = forms.CharField(label="First name", max_length=)
    lname = forms.CharField(label="Last name", max_length=)
    email = forms.EmailField(label="Email", max_length=)
    username = forms.CharField(label="Username", max_length=100, placeholder="sarakhan")
    password = forms.CharField(label="First name", max_length=)
    cPassword = forms.CharField(label="First name", max_length=)




