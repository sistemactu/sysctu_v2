from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActaForm
from .models import Acta

#agregar actas
def acta_new(request):
    if request.method == 'POST':
        form = ActaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('actas')
    else:
        form =  ActaForm()
    return render(request, 'actas/reg_acta.html', {'form':form})

#listar actas
def acta_list(request):
    actas = Acta.objects.all().order_by('-fechaActa')
    contexto = {'actas': actas}       
    return render(request, 'actas/listar_actas.html',  contexto)

#seleccionar acta
def acta_detail(request, pk):
    acta = get_object_or_404(Acta, pk=pk)
    contexto = {'acta': acta}
    return render(request, 'actas/detalle_acta.html', contexto)

#editar acta
def acta_edit(request, pk):
    acta = get_object_or_404(Acta, pk=pk)
    if request.method == "POST":
        form = ActaForm(request.POST, instance=acta)
        if form.is_valid():
            acta.save()
            return redirect('detalle_acta', pk=acta.pk)
    else:
        form = ActaForm(instance=acta)
    return render(request, 'actas/reg_acta.html', {'form': form})


#borrar acta
def acta_delete(request, pk, template_name='actas/actas_confirm_delete.html'):
    acta= get_object_or_404(Acta, pk=pk)    
    if request.method=='POST':
        acta.delete()
        return redirect('listar_actas')
    return render(request, template_name, {'object':acta})

