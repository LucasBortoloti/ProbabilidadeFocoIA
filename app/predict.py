import joblib
import numpy as np
import pandas as pd

# Carregar o modelo treinado
modelo = joblib.load("models/modelo_rf.pkl")

def prever_foco(temperatura_c, umidade, precipitacao_mm):
    # Criar o DataFrame com os dados de entrada
    dados_entrada = pd.DataFrame({
        "temperatura_c": [temperatura_c],
        "umidade": [umidade],
        "precipitacao_mm": [precipitacao_mm]
    })

    # Realizar a previsão de foco (classe) e probabilidade
    previsao = modelo.predict(dados_entrada)
    probabilidade = modelo.predict_proba(dados_entrada)

    # A previsão é o foco_id
    foco_predito = int(previsao[0])

    # A probabilidade é a probabilidade da classe prevista
    probabilidade_foco = probabilidade[0][modelo.classes_.tolist().index(foco_predito)]

    return foco_predito, probabilidade_foco

