from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Recipe

def index(request):
    receitas = Recipe.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Recipe, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)

def buscar(request):
    lista_receitas = Recipe.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_da_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
