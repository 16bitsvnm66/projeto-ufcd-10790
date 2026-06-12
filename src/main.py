import json
import os
from datetime import datetime

FICHEIRO_RESERVAS = "reservas.json"
MESAS = [1, 2, 3, 4, 5, 6, 7, 8]
RESTAURANTES = [
    {
        "id": 1,
        "nome": "Tasca do Zé",
        "cozinha": "Portuguesa",
        "cidade": "Lisboa",
        "morada": "Rua das Flores, 12",
        "avaliacao_total": 0,
        "num_avaliacoes": 0
    },
    {
        "id": 2,
        "nome": "Marisqueira Atlântico",
        "cozinha": "Mariscos",
        "cidade": "Cascais",
        "morada": "Av. Marginal, 88",
        "avaliacao_total": 0,
        "num_avaliacoes": 0
    },
    {
        "id": 3,
        "nome": "Sushi Nagoya",
        "cozinha": "Japonesa",
        "cidade": "Lisboa",
        "morada": "Rua do Carmo, 45",
        "avaliacao_total": 0,
        "num_avaliacoes": 0
    },
    {
        "id": 4,
        "nome": "La Piazza",
        "cozinha": "Italiana",
        "cidade": "Porto",
        "morada": "Rua Augusta, 201",
        "avaliacao_total": 0,
        "num_avaliacoes": 0
    },
    {
        "id": 5,
        "nome": "Adega Alentejana",
        "cozinha": "Alentejana",
        "cidade": "Évora",
        "morada": "Praça do Comércio, 3",
        "avaliacao_total": 0,
        "num_avaliacoes": 0
    },
]


def carregar_reservas():
    if os.path.exists(FICHEIRO_RESERVAS):
        with open(FICHEIRO_RESERVAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_reservas(reservas):
    with open(FICHEIRO_RESERVAS, "w", enconding="utf-8") as f:
        json.dump(reservas, f, indent=4)

def obter_restaurante(restaurante_id):
    for restaurante in RESTAURANTES:
        if restaurante["id"] == restaurante_id:
            return restaurante
 
def mostrar_restaurantes():
    print("\n======== RESTAURANTES DISPONÍVEIS ========")
    print(f"  {'ID':<4} {'NOME':<26} {'COZINHA':<14} {'CIDADE'}")
    print("  " + "─" * 58)
    for r in RESTAURANTES:
        # Calcula a média de avaliação para mostrar ao lado
        if r["num_avaliacoes"] > 0:
            media = r["avaliacao_total"] / r["num_avaliacoes"]
            estrelas = f"  ★ {media:.1f}"
        else:
            estrelas = "  (sem avaliações)"
        print(f"  [{r['id']}]  {r['nome']:<26} {r['cozinha']:<14} {r['cidade']}{estrelas}")



def gerar_codigo_reserva(reservas):
    numero = len(reservas) + 1
    return f"R{numero:04d}"

def atribuir_mesas(reservas, data, hora, restaurante_id):
    mesas_ocupadas = []
    
    for reserva in reservas:
        if reserva["data"] == data and reserva["hora"] == hora and reserva["restaurante_id"] == restaurante_id:
            mesas_ocupadas.append(reserva["mesa"])
    for mesa in Mesas:
        if mesa not in mesas_ocupadas:
            return mesa
    return None

def calcular_dias_para_reserva(data):
    data_reserva = datetime.strptime(data, "%d-%m-%Y").date()
    hoje = datetime.now().date()

    return (data_reserva - hoje).days

def criar_reserva(reservas):
    print("\n======== CRIAR RESERVA ========")
    restaurante = escolher_restaurante()
    print(f"\nRestaurante escolhido: {restaurante['nome']} - {restaurante['morada']}, {restaurante['cidade']}")
    
    nome = input("Nome do cliente: ")

    while True: 
        data = input("Data da reserva (dd-mm-aaaa): ")

        try:
            data_reserva = datetime.strptime(data, "%d-%m-%Y").date()
            hoje = datetime.now().date()

            if data_reserva < hoje:
                print("A data da reserva não pode ser no passado. Tente novamente.")
                continue
            break
        except ValueError:
            print("Formato de data inválido. Use dd-mm-aaaa. Tente novamente.")
    
    hora = input("Hora da reserva (hh:mm): ")
    pessoas = int(input("Número de pessoas: "))
    mesa = atribuir_mesas(reservas, data, hora)

    if mesa is None:
        print("\nDesculpe, não há mesas disponíveis para essa data e hora.")
        return
    
    codigo_reserva = gerar_codigo_reserva(reservas)

    dias_faltam = (data_reserva - hoje).days

    if dias_faltam == 0:
        print("A reserva é para hoje! Por favor, chegue com antecedência.")
    else:
        print(f"Faltam {dias_faltam} dias para a reserva.")

    return {
        "codigo": codigo_reserva,
        "nome": nome,
        "data": data,
        "hora": hora,
        "pessoas": pessoas,
        "mesa": mesa,
        "restaurante_id": restaurante["id"],
        "avaliacao": None

    }



def adicionar_reserva(reservas):
    reserva = criar_reserva(reservas)

    if reserva is not None:
        reservas.append(reserva)
        guardar_reservas(reservas)

        print("\nReserva adicionada com sucesso!")
        print(f"Código da reserva: {reserva['codigo']}")
        print(f"Mesa atribuída: {reserva['mesa']}")

def listar_reservas(reservas):
    if not reservas:
        print("\nNenhuma reserva encontrada.")
        return
    
    print("\n======== LISTA DE RESERVAS ========")

    for indice, reserva in enumerate(reservas, start=1):
        print(f"{indice}. Código: {reserva['codigo']}, Nome: {reserva['nome']}, Data: {reserva['data']}, Hora: {reserva['hora']}, Pessoas: {reserva['pessoas']}, Mesa: {reserva['mesa']}")

def pesquisar_reserva(reservas):
    if not reservas:
        print("\nNenhuma reserva encontrada.")
        return
    
    pesquisa = input("\nDigite o seu nome ou código de reserva: ").lower()
    econtradas = []

    for reserva in reservas:
        if pesquisa in reserva["nome"].lower() or pesquisa == reserva["codigo"].lower():
            econtradas.append(reserva)
    
    if not econtradas:
        print("\nNenhuma reserva encontrada com esse nome ou código.")
        return
    
    print("\n======== RESERVAS ENCONTRADAS ========")

    for reserva in econtradas:
        print(f"Código: {reserva['codigo']}, Nome: {reserva['nome']}, Data: {reserva['data']}, Hora: {reserva['hora']}, Pessoas: {reserva['pessoas']}, Mesa: {reserva['mesa']}")

def cancelar_reserva(reservas):
    if not reservas:
        print("\Nenhuma reserva encontrada.")
        return
    
    codigo = input("\nDigite o código da reserva que deseja cancelar: ").upper()

    for reserva in reservas:
        if reserva["codigo"] == codigo:
            reservas.remove(reserva)
            guardar_reservas(reservas)
            print(f"\nReserva {codigo} cancelada com sucesso!")
            
            return
        
    print("\nNenhuma reserva encontrada com esse código.")

def mostrar_menu():
    print("\n======== SISTEMA DE RESERVAS ========")
    print("1. Adicionar reserva")
    print("2. Listar reservas")
    print("3. Pesquisar reserva")
    print("4. Cancelar reserva")
    print("5. Sair")





