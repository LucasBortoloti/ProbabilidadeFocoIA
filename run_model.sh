#!/bin/bash
cd /home/usuario/Downloads/inteligenciaartificialexemplo && \
python3 -m venv venv && \
. venv/bin/activate && \
pip install fastapi uvicorn pandas numpy scikit-learn xgboost joblib sqlalchemy pymysql apscheduler && \
python -m app.train_model && \
nohup uvicorn app.api:app --reload &
