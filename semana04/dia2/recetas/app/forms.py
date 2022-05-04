from django import forms

class RecetaForm(forms.Form):
    titulo = forms.CharField(label='Titulo',max_length=100,required=True)
    ingredientes = forms.CharField(label='Ingredientes',widget=forms.Textarea)
    preparacion = forms.CharField(label='Preparación',widget=forms.Textarea)
    autor = forms.CharField(label='Autor',max_length=200,required=True)