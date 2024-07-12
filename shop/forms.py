from .models import Produto
from django import forms

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'preco', 'preco_promocional', 'desconto', 'foto', 'estrela')
        widgets = {
          'nome': forms.TextInput(attrs={'class': 'form-control'}),
          'preco': forms.NumberInput(attrs={'class': 'form-control'}),
          'preco_promocional': forms.NumberInput(attrs={'class': 'form-control'}),
          'desconto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
          'estrela': forms.Select(attrs={'class': 'form-control'}),
          'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }