from statistics import mean


def lista_numeros(lista: list):
    lista_numeros = lista
    total = sum(lista_numeros)
    media = mean(lista_numeros)
    quantidade = len(lista_numeros)

    return total, media, quantidade


lista = [12, 45, 78, 84, 51, 26, 59,]
total, media, quantidade = lista_numeros(lista)
print(f'Total: {total}')
print(f'Média: {media}')
print(f'Quantidade de elementos: {quantidade}')
