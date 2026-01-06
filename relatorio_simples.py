from random import randint


def dados_fake(quantidade: int):
    lista_nomes = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda",
        "Gabriel", "Helena", "Igor", "Juliana", "Breno",
        "Kleber", "Larissa", "Marcos", "Natália", "Otávio", "Patrícia",
        "Quésia", "Rafael", "Sabrina", "Tiago", "Camila",
        "Ursula", "Vinícius", "Wagner", "Xênia", "Yasmin", "Zeca", "Alice",
        "Elisa", "Felipe", "Giovana", "Henrique", "Isabela", "João", "Karen",
        "Lucas", "Marta", "Nicolas", "Valéria", "William", "Xavier", "Diego",
        "Olívia", "Paulo", "Queila", "Rodrigo", "Simone", "Talita", "Ulisses",
    ]
    lista_idades = [
        23, 45, 18, 34, 56, 29, 41, 67, 12, 38, 25, 19, 69, 72, 15, 48, 33, 27,
        54, 39, 22, 46, 70, 65, 32, 24, 59, 13, 67, 43, 49, 30, 10, 13, 17, 11,
        21, 44, 31, 50, 26, 37, 42, 16, 58, 68, 20, 35, 47, 14, 53, 40, 28, 36,
    ]
    dicionario = {}
    lista_retorno = []

    for item in range(quantidade):
        dicionario['nome'] = lista_nomes[randint(0, 49)]
        dicionario['idade'] = lista_idades[randint(0, 49)]
        lista_retorno.append(dicionario.copy())

    return lista_retorno


def contagem_dados(lista: list):
    return f'Total de elementos é: {len(lista)}'


def classificacao_idades(lista: list):
    classificacao = []
    for item in lista:
        if item.get('idade') < 18:
            item['classificação'] = 'Menor de Idade'
        elif item.get('idade') > 65:
            item['classificação'] = 'Idoso'
        else:
            item['classificação'] = 'Adulto'
        classificacao.append(item.copy())
    return classificacao


lista_fake = dados_fake(6)
print(f'Dados: {lista_fake}')
print(contagem_dados(lista_fake))
print(classificacao_idades(lista_fake))
