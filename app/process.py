import pandas as pd

def carregar_dados():
    # Carregar os dados climáticos
    clima = pd.read_csv("data/clima.csv")

    # Carregar os dados de focos de dengue
    focos = pd.read_csv("data/foco.csv")

    # Renomeando as colunas de data nos dois DataFrames
    focos.rename(columns={'data_hora': 'data'}, inplace=True)  # 'data_hora' para 'data'
    clima.rename(columns={'data_registro': 'data'}, inplace=True)  # 'data_registro' para 'data'

    # Unir as duas bases de dados
    dados = pd.merge(focos, clima, on='data', how='left')

    print(dados.columns)

    # Tratar valores ausentes
    dados.fillna(0, inplace=True)

    return dados
