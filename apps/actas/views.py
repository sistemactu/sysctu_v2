from django.shortcuts import render, redirect
from apps.actas.forms import ActaForm


def acta_new(request):
    if request.method == 'POST':
        form = ActaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form =  ActaForm()
    return render(request, 'actas/reg_acta.html', {'form':form})
