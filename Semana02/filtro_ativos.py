import pandas as pd


def filtrar_ativos(dados):
    registros = pd.read_csv(dados)
    ativos = registros[registros['ativo'] == True].count()
    return ativos


quantidade_ativos = filtrar_ativos('dados.csv')
print(f'O total de registros ativos são {quantidade_ativos['ativo']}')
