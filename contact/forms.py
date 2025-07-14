from django.db import models
from django import forms

# Create your models here.
class ContactForm(forms.Form):
    name= forms.CharField(label="Nombre", required=True, widget = forms.TextInput(attrs={"placeholder": "Escribe tu nombre", "class":"form-control"}))
    email= forms.EmailField(label="Email", required=True, widget = forms.TextInput(attrs={"placeholder": "Escribe tu email", "class":"form-control"}))
    content= forms.CharField(label="Contenido",required=True, widget=forms.Textarea(attrs={"placeholder": "Escribe tu email", "rows":3, "class":"form-control"}))
    
    