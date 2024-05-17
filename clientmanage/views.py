from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator

from . import forms, models


@login_required
def home(request):
    client = models.Client.objects.all()
    assurance = models.Assurances.objects.all()

    context = {
        'clientlist': client,
        'assurancelist': assurance
    }
    return render(request, 'clientmanage/home.html')



@login_required
def crateclient(request):
    clientForm = forms.ClientForm()

    if request.method == 'POST':
        clientForm = forms.ClientForm(request.POST)
        if clientForm.is_valid():
            clientForm.save()
            return redirect('home')

    contest = {
        'clientForm' : clientForm
    }

    return render(request, 'crateclient/.html')
