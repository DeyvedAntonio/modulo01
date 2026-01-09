from random import randint

lista_idade = [randint(1, 90) for valor in range(500)]

lista_menores = []
lista_adultos = []
lista_idosos = []

for idade in lista_idade:
    if idade < 18:
        lista_menores.append(idade)
    elif idade > 65:
        lista_idosos.append(idade)
    else:
        lista_adultos.append(idade)

print(f'Menores {lista_menores}')
print(f'Menores: {len(lista_menores)}')
print(f'Adultos {lista_adultos}')
print(f'Adultos: {len(lista_adultos)}')
print(f'Idosos {lista_idosos}')
print(f'Idosos: {len(lista_idosos)}')
