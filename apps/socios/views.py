from django.shortcuts import render, redirect
from apps.socios.models import Socio
from apps.socios.forms import SocioForm


def agregarsocio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('../socios')

    else:
        form =  SocioForm()

    return render(request, 'socios/solicitudform.html', {'form':form})
