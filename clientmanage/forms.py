from django import forms

from . import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['nom', 'prenom', 'email']  # Excluez 'uploader' et 'date_created'


class AssurancesForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['type', 'date_debut', 'date_fin', 'client']  # Excluez 'uploader' et 'date_created'


