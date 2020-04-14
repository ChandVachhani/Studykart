from django import forms

class edit_profile(forms.Form):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'ufname',
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'ulname',
    }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'uname',
    }))
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'uemail',
    }))
    mobile = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'umobile',
    }))


class signin_card(forms.Form):
    identifier = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control text-black',
                                                               'style': 'font-size: 18px !important;',
                                                               'id': 'uname'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-black',
        'id': 'pass',
        'style': 'font-size: 18px !important;',
    }))
