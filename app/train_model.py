from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from app.process import carregar_dados

def treinar_modelo():
    # Carregar e preparar os dados
    dados = carregar_dados()

    # Definir as features e o alvo
    X = dados[["temperatura_c", "umidade", "precipitacao_mm"]]
    y = dados["foco_id"]

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar e treinar o modelo
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Salvar o modelo treinado
    joblib.dump(modelo, "models/modelo_rf.pkl")

    print("✅ Modelo treinado e salvo com sucesso!")

# Se o script for executado diretamente, treinar o modelo
if __name__ == "__main__":
    treinar_modelo()
