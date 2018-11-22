from django.shortcuts import render, redirect
from apps.socios.models import Socio
from apps.socios.forms import SocioForm
from django.utils import timezone


#crear solicitudes
def agregarsocio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST, request.FILES)
        if form.is_valid():
            socio = form.save(commit=False)
            socio.estSolic = 'p'
            socio.fecSolic = timezone.now()
            socio.save()
        return redirect('listar_solicitudes')
        
    else:
        form =  SocioForm()
    return render(request, 'socios/solicitudform.html', {'form':form})


#listar solicitudes
def solic_list(request):
    socios = Socio.objects.all().exclude(estSolic='a').order_by('-fecSolic')
    contexto = {'socios': socios}       
    return render(request, 'socios/listar_socios.html',  contexto)

#listar solicitudes
def socio_list(request):
    socios = Socio.objects.all()
    contexto = {'socios': socios}       
    return render(request, 'socios/listar_socios.html',  contexto)