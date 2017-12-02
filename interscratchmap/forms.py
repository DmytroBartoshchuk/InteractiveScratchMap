from django import forms

class NameForm(forms.Form):
    email_adress = forms.CharField(label='Adress Email\n', max_length=100)
    your_name = forms.CharField(label='Message', max_length=1000 )
