from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from app.predict import prever_foco

# Carregar o modelo treinado
modelo = joblib.load("models/modelo_rf.pkl")  # Use o modelo correto

# Inicializar o FastAPI
app = FastAPI()

# Definir o modelo de dados esperado
class PrevisaoInput(BaseModel):
    temperatura_c: float
    umidade: float
    precipitacao_mm: float

@app.post("/previsao/")
async def previsao(input_data: PrevisaoInput):
    # Criar um DataFrame com as entradas
    dados_entrada = pd.DataFrame([input_data.dict()])
    
    # Fazer a previsão
    previsao, probabilidade = prever_foco(dados_entrada['temperatura_c'][0], 
                                          dados_entrada['umidade'][0], 
                                          dados_entrada['precipitacao_mm'][0])
    
    # Converte a probabilidade para porcentagem
    probabilidade = probabilidade * 100
    
    # Retornar o resultado
    return {"previsao": previsao, "probabilidade": probabilidade}
