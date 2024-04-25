from django.shortcuts import render
from medico.views import DadosMedico,Especialidades
# Create your views here.

def home(request):
    if request.method == 'GET':
        medico_filtrar = request.GET.get('medico')
        especialidade_filtrar = request.GET.getlist('especialidades')
        medicos = DadosMedico.objects.all()

        if medico_filtrar:
            medicos = medicos.filter(nome__icontains=medico_filtrar)
        
        if especialidade_filtrar:
            medicos = medicos.filter(especialiade_id__in=especialidade_filtrar)
        especialidades = Especialidades.objects.all()
        return render(request,'home.html', {'medicos':medicos, 'especialidades': especialidades})