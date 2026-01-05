from random import random
from statistics import mean


valores_vendas = [random() * 100 for valor in range(15)]

total_vendas = sum(valores_vendas)
media_vendas = mean(valores_vendas)
maior_valor = max(valores_vendas)
menor_valor = min(valores_vendas)

print(f'Total de vendas: R$ {total_vendas:.2f}')
print(f'A média das vendas é : R$ {media_vendas:.2f}')
print(f'O maior valor de vendas é: R$ {maior_valor:.2f}')
print(f'O menor valor de vendas é: R$ {menor_valor:.2f}')
