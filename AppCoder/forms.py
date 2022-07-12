from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    emails = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    emails = forms.EmailField()
    
class EntregableFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
