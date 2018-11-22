from django.shortcuts import render, redirect
from apps.socios.models import Socio
from apps.socios.forms import SocioForm


#crear solicitudes
def agregarsocio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('socios')
    else:
        form =  SocioForm()
    return render(request, 'socios/solicitudform.html', {'form':form})


#listar socios
def socio_list(request):
    socios = Socio.objects.all()
    contexto = {'socios': socios}       
    return render(request, 'socios/listar_socios.html',  contexto)