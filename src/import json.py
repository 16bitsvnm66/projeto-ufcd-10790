import json
import os
from datetime import datetime

FICHEIRO_RESERVAS = "reservas.json"
Mesas = [1, 2, 3, 4, 5, 6, 7, 8]

def carregar_reservas():
    if os.path.exists(FICHEIRO_RESERVAS):
        with open(FICHEIRO_RESERVAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_reservas(reservas):
    with open(FICHEIRO_RESERVAS, "w", enconding="utf-8") as f:
        json.dump(reservas, f, indent=4)

def gerar_codigo_reserva(reservas):
    numero = len(reservas) + 1
    return f"R{numero:04d}"

def atribuir_mesas(reservas, data, hora):
    mesas_ocupadas = []
    
    for reserva in reservas:
        if reserva["data"] == data and reserva["hora"] == hora:
            mesas_ocupadas.append(reserva["mesa"])
    for mesa in Mesas:
        if mesa not in mesas_ocupadas:
            return mesa
    return None

def calcular_dias_para_reserva(data):
    data_reserva = datetime.strptime(data, "%d-%m-%Y").date()
    hoje = datetime.now().date()

    return (data_reserva - hoje).days

