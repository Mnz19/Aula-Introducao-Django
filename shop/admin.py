from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'preco_promocional', 'desconto', 'estrela')
    search_fields = ('nome',)
    list_filter = ('desconto', 'estrela')