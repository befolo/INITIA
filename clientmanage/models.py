from django.db import models
import datetime


class Client(models.Model):
    nom = models.CharField(max_length=128, verbose_name='nom')
    prenom = models.CharField(max_length=128, verbose_name='prenom')
    email = models.EmailField(unique=True)


class Assurances(models.Model):
    TYPEA = 'TYPEA'
    TYPEB = 'TYPEB'

    TYPES_CHOICE = (
        (TYPEA, 'type B'),
        (TYPEB, 'type A'),
    )

    type = models.CharField(max_length=30, choices=TYPES_CHOICE, verbose_name='Type d\'assurance')
    date_debut = models.DateField(default=datetime.date.today, verbose_name="Date de debut")
    date_fin = models.DateField(default=datetime.date.today, verbose_name="Date de fin")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)


