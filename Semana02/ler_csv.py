import pandas as pd


def carregar_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados


novos_dados = carregar_dados('dados.csv')
print(novos_dados)
