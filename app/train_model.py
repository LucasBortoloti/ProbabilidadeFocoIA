from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

from app.process import carregar_dados

# Carregar e preparar os dados
dados = carregar_dados()

# Definir as features e o alvo
X = dados[["temperatura_c", "umidade", "precipitacao_mm"]]
y = dados["foco_id"]

# Verificar as classes em y
print("Classes únicas em y:", y.unique())

# Se necessário, mapear as classes para o intervalo correto
# Supondo que as classes sejam 7, 8, 9, 10 e você queira transformá-las para 0, 1, 2, 3
y = y.replace({7: 0, 8: 1, 9: 2, 10: 3})

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
modelo = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
modelo.fit(X_train, y_train)

# Salvar o modelo treinado
joblib.dump(modelo, "models/modelo_xgb.json")
