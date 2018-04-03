from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def todosChamados(request, template_name='todos.html'):
    chamado = Chamado.objects.all()
    chamados = {'chamados': chamado}
    return render(request, template_name, chamados)

def chamadoID(request, pk):
    id = get_object_or_404(Chamado, pk=pk)
    return render(request,{'id' : id})

def atendimentosConcluidos(request):
    retorno = "Todos os atendimentos concluidos"
    lista = Atendimento.objects.filter(Atendimento__status='Concluído')
    for i in lista:
        retorno += 'Título do chamado: {} <br>'.format(i.titulo)
    return HttpResponse(retorno)