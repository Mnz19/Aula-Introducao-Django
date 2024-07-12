from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
    path('detalhes/<int:pk>/', detalhes_produto, name='detalhes_produto'),
    path('editar/<int:pk>/', editar_produto, name='editar_produto'),
    path('deletar/<int:pk>/', deletar_produto, name='deletar_produto')
]
