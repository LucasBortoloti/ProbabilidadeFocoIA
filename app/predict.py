import joblib
import numpy as np
import pandas as pd

# Carregar o modelo treinado
modelo = joblib.load("models/modelo_rf.pkl")

def prever_foco(temperatura_c, umidade, precipitacao_mm):
    dados_entrada = pd.DataFrame({
        "temperatura_c": [temperatura_c],
        "umidade": [umidade],
        "precipitacao_mm": [precipitacao_mm]
    })

    previsao = modelo.predict(dados_entrada)[0]
    probabilidade = modelo.predict_proba(dados_entrada)[0]

    print(f"Previsão: {previsao}")
    print(f"Probabilidades: {probabilidade}")

    foco_predito = int(previsao)
    probabilidade_foco = probabilidade[modelo.classes_.tolist().index(foco_predito)]

    print(f"Foco predito: {foco_predito}, Probabilidade: {probabilidade_foco}")

    return foco_predito, probabilidade_foco
