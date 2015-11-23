from django import forms

# import datetime

class FormularioLogin(forms.Form):
    user = forms.CharField(required=True, label='Usuario', widget=forms.TextInput())
    passwd = forms.CharField(required=True, label='Clave', widget=forms.PasswordInput())
    #image = forms.ImageField(required= False)
    #day = forms.DateField(initial=datetime.date.today())

class FormularioContacto(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea())