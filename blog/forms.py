from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Artikel

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'body', 'kategori')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'placeholder' : "Judul Artikel",
                    'required' : True
                }),
             #cols="30" rows="10" class="form-control"
            "body" : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'cols' : '30',
                    'row' : '10',
                    'required' : True
                }),
            "kategori" : forms.Select(
                attrs={
                    'class' : 'selectpicker',
                    'required' : True,
                    'data-style' : 'btn btn-danger btn-block',
                    'title' : 'Pilih Kategori',
                    'data-size' : '7',
                }),
        }