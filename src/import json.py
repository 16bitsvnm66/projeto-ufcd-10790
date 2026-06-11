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

