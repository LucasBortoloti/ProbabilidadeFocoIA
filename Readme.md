## Para rodar essa aplicação:

Não necessita mais dos CSVS pq puxa direto do banco

## Criar ambiente virtual

python3 -m venv venv

source venv/bin/activate  # Ativa o ambiente virtual

## Instalar bibliotecas

pip install fastapi uvicorn pandas numpy scikit-learn xgboost joblib sqlalchemy pymysql apscheduler

## Ajustar o arquivo process.py

Ajustar as configurações do banco de dados

## Para treinar e gerar o arquivo (modelo_rf.pkl) a partir dos bancos de dados

python -m app.train_model

caso ele já esteja criado vai estar na pasta (models)

## Rodar API

uvicorn app.api:app --reload

## Para ver a probabilidade de foco:

ter o Insomnia instalado

fazer um POST com essa URL http://127.0.0.1:8000/previsao/

e no body colocar o seguinte JSON:

{
  "temperatura_c": 30,
	"umidade": 92,
  "precipitacao_mm": 5
}

assim retornará: 

{
	"previsao": 1,
	"probabilidade": 43.599999999999994
}

Mas óbvio que os valores podem ser mudados para testar diferentes cenários.

## Rodar o agendador (para re-treinar o modelo automaticamente a cada 30 minutos) usando o arquivo run_model.sh e o Cron

Configure o Cron:

contrab -e

Adicione o seguinte comando:

*/30 * * * * /home/usuario/Downloads/inteligenciaartificialexemplo/run_model.sh >> /home/usuario/Downloads/inteligenciaartificialexemplo/logs/cron.log 2>&1

Verifique se o diretório está correto, pois pode variar

Para conferir as logs do cron é só vizualizar o arquivo da pasta logs/cron.log

:D
