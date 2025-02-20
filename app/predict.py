import joblib
import numpy as np

# Carregar o modelo treinado
modelo = joblib.load("models/modelo_xgb.json")

# Função de previsão
def prever_foco(temperatura, umidade, precipitacao):
    print(f"Temperatura: {temperatura}, Umidade: {umidade}, Precipitação: {precipitacao}")
    
    # Simulação de um modelo de previsão para exemplo
    # Suponha que o modelo deve retornar uma previsão com base nos dados
    previsao = temperatura * 0.5 + umidade * 0.3 + precipitacao * 0.2
    probabilidade = 1 / (1 + np.exp(-previsao))  # Exemplo de função logística para probabilidade
    
    print(f"Previsão calculada: {previsao}, Probabilidade calculada: {probabilidade}")
    
    return previsao, probabilidade
