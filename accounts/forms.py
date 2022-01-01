from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.forms import Form, TextInput


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))
    
#class TextSearchForm(Form):
    #def __init__(self, *args, **kwargs):
        #super(Form, self).__init__(*args, **kwargs)

    #search_input = TextInput(
        #attrs={'class': 'form-control', 'placeholder': 'Text Search'})
    