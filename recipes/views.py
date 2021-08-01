from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Recipe

def index(request):
    receitas = Recipe.objects.filter(publicada=True)

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
