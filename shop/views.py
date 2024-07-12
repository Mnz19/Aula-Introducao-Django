from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
# Create your views here.

def home(request):
    context = {
        'nome': 'Django E-Commerce',
        'descricao': 'Sua loja de produtos favorita!',
        'produtos': Produto.objects.all(),
    }
    return render(request, 'produtos.html', context)

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
        
    return render(request, 'form.html', {'form': form})

def detalhes_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    return render(request, 'detalhes.html', {'produto': produto})

def editar_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'form.html', {'form': form})

def deletar_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('home')