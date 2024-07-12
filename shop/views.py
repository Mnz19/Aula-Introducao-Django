from django.shortcuts import render
from .models import Produto
# Create your views here.

def home(request):
    context = {
        'nome': 'Django E-Commerce',
        'descricao': 'Sua loja de produtos favorita!',
        'produtos': Produto.objects.all(),
    }
    return render(request, 'produtos.html', context)