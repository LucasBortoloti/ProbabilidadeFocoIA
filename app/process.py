from sqlalchemy import create_engine
import pandas as pd

# Configuração da conexão com o banco
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""  # Ou IP do servidor
DB_NAME = ""

# Criar engine de conexão
engine = create_engine(f"mysql+pymysql://(DB_USER):(DB_PASSWORD)@(DB_HOST)/(DB_NAME)") # remover os parenteses quando arrumar as informação corretas

def carregar_dados():
    # Query para buscar os dados da view
    query = """
    SELECT foco_id, temperatura_c, umidade, precipitacao_mm
    FROM foco_clima_view
    """

    # Ler os dados direto do banco de dados
    dados = pd.read_sql(query, engine)

    # Tratar valores ausentes
    dados.fillna(0, inplace=True)

    return dados