from random import random


lista = [valor * random() * 10 for valor in range(20)]
lista_valido = []
lista_invalido = []

for item in lista:
    if item > 15:
        lista_valido.append(item)
    else:
        lista_invalido.append(item)

print(lista)
print(lista_valido)
print(lista_invalido)
