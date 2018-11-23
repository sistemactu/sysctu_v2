from django.shortcuts import render, redirect, get_object_or_404
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
            socio.totPag = socio.cuotInc + socio.cuotSoc

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

#listar socios
def socio_list(request):
    socios = Socio.objects.filter(estSolic='a').order_by('-fecSolic')
    contexto = {'socios': socios}       
    return render(request, 'socios/listar_socios.html',  contexto)

#seleccionar socio
def socio_detail(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    contexto = {'socio': socio}
    return render(request, 'actas/detalle_socio.html', contexto)

#editar solicitudes
def socio_edit(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == "POST":
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            socio.save()
            return redirect('listar_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socios/solicitudform.html', {'form': form})