from django.db import models

class Produto(models.Model):
    ESTRELAS_CHOICES = (
      (1, '1 estrela'),
      (2, '2 estrelas'),
      (3, '3 estrelas'),
      (4, '4 estrelas'),
      (5, '5 estrelas'),
    )
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='produtos', null=True, blank=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    preco_promocional = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.BooleanField(default=False)
    estrela = models.IntegerField(choices=ESTRELAS_CHOICES)
    
    def __str__(self):
        return self.nome.capitalize()
      