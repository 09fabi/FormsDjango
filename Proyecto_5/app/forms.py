from django import forms

class Registrousuario(forms.Form):
    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloqueado', 'BLOQUEADO')]

    nombre = forms.CharField()
    telefono = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'