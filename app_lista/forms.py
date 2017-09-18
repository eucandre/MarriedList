from django import forms
from .models import *

class FormCasal(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    data_evento= forms.DateField(label='Data do Casamento', widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    class Meta:
        model = Casal
        fields = ('nome','data_evento')

class FormPresente(forms.ModelForm):
    class Meta:
        model = Presente
        fields = ('nome','valor')

class FormDesejos(forms.ModelForm):
    casal= forms.ModelChoiceField(label='Casal', queryset=Desejos.objects.all(), widget=forms.Select(attrs={'type':'select','class':'form-control'}))
    desejo = forms.ModelMultipleChoiceField(label='Desejo(s)',queryset=Desejos.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'type':'select'}))
    class Meta:
        model = Desejos
        fields = ('casal', 'desejo')
