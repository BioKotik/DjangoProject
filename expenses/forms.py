from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SendEmailForm(forms.Form):
    my_email = forms.CharField(max_length=100)
    address = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)
