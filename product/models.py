from django.db import models


class Product(models.Model):
    description = models.CharField('Nome do Produto', max_length=150)
    price = models.DecimalField('Preço do produto', decimal_places=2, max_digits=6)
    stock = models.IntegerField('Estoque Disponível')
    stock_min = models.IntegerField('Mínimo estoque aceitável')

    def __str__(self):
        return f'Produto ( {self.description} ) - Preço Unt ( {self.price} ) - Qtd em estoque ( {self.stock} ) '
