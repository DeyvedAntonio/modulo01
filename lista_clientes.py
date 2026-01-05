from random import choice


nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Kleber", "Larissa", "Marcos", "Natália", "Otávio"
]
perfil = [True, False]
clientes = []
pessoa = {}

for nome in nomes:
    pessoa['nome'] = nome
    pessoa['ativo'] = choice(perfil)
    clientes.append(pessoa.copy())

total_cliente = len(clientes)
total_ativo = len([cliente.get('nome') for cliente in clientes if cliente.get('ativo')])
total_inativo = len([cliente.get('nome') for cliente in clientes if not cliente.get('ativo')])

print('='*22)
print('Relatórios de Clientes')
print('='*22)
print(f'Total de clientes é {total_cliente}')
print(f'Total de clientes ativos é {total_ativo}')
print(f'Total de clientes inativos é {total_inativo}')
print('-'*22)
