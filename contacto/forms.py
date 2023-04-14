from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    telefono = forms.CharField(label="Teléfono", required=False)
    email = forms.CharField(label="Email", required=True)
    contenido = forms.CharField(label="Tu propuesta", widget=forms.Textarea)