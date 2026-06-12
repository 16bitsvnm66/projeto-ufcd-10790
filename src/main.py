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
# --------------------------------------------------
#                 PERSISTÊNCIA
# --------------------------------------------------

def carregar_reservas():
    if os.path.exists(FICHEIRO_RESERVAS):
        with open(FICHEIRO_RESERVAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_reservas(reservas):
    with open(FICHEIRO_RESERVAS, "w", encoding="utf-8") as f:
        json.dump(reservas, f, indent=4)

#--------------------------------------------------
#               RESTAURANTES
# --------------------------------------------------

def obter_restaurante(restaurante_id):
    for restaurante in RESTAURANTES:
        if restaurante["id"] == restaurante_id:
            return restaurante
 
def mostrar_restaurantes():
    print("\n======== RESTAURANTES DISPONÍVEIS ========")
    print(f"  {'ID':<4} {'NOME':<26} {'COZINHA':<14} {'CIDADE'}")
    print("  " + "─" * 58)
    
    for r in RESTAURANTES:
        if r["num_avaliacoes"] > 0:
            media = r["avaliacao_total"] / r["num_avaliacoes"]
            estrelas = f"  ★ {media:.1f}"
        else:
            estrelas = "  (sem avaliações)"
        print(f"  [{r['id']}]  {r['nome']:<26} {r['cozinha']:<14} {r['cidade']}{estrelas}")

def escolher_restaurante():
    mostrar_restaurantes()
    print()
 
    while True:
        try:
            escolha = int(input("  Escolha o número do restaurante: "))
            restaurante = obter_restaurante(escolha)
            if restaurante:
                return restaurante
            print("  Número inválido. Tente novamente.")
        except ValueError:
            print("  Introduza um número válido.")

def avaliar_restaurante(reservas):
   
    if not reservas:
        print("\nNão existem reservas. Faça uma reserva primeiro.")
        return
 
    codigo = input("\nDigite o código da reserva para avaliar: ").upper()
 
    reserva_encontrada = None
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            reserva_encontrada = reserva
            break
 
    if reserva_encontrada is None:
        print("Nenhuma reserva encontrada com esse código.")
        return
 
    if reserva_encontrada.get("avaliacao"):
        print(f"\nJá avaliou este restaurante com {reserva_encontrada['avaliacao']} estrelas.")
        return
 
    nome_restaurante = reserva_encontrada.get("restaurante")
    print(f"\nAvaliar: {nome_restaurante}")
 
    while True:
        try:
            nota = int(input("Nota de 1 a 5 estrelas: "))
            if 1 <= nota <= 5:
                break
            print("Introduza um número entre 1 e 5.")
        except ValueError:
            print("Introduza um número válido.")
 
   
    reserva_encontrada["avaliacao"] = nota
 

    for r in RESTAURANTES:
        if r["nome"] == nome_restaurante:
            r["avaliacao_total"] += nota
            r["num_avaliacoes"] += 1
            media = r["avaliacao_total"] / r["num_avaliacoes"]
            print(f"\n✓ Avaliação registada! {'★' * nota}{'☆' * (5 - nota)}")
            print(f"  Média atual de {nome_restaurante}: {media:.1f} estrelas")
            break
 
    guardar_reservas(reservas)

#--------------------------------------------------
#                  RESERVAS
#--------------------------------------------------



def gerar_codigo_reserva(reservas):
    numero = len(reservas) + 1
    return f"R{numero:04d}"

def atribuir_mesas(reservas, data, hora, restaurante_id):
    mesas_ocupadas = []
    
    for reserva in reservas:
        if reserva["data"] == data and reserva["hora"] == hora and reserva["restaurante_id"] == restaurante_id:
            mesas_ocupadas.append(reserva["mesa"])
    for mesa in MESAS:
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
    mesa = atribuir_mesas(reservas, data, hora, restaurante["id"])

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
        "restaurante": restaurante["nome"],
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
        avaliacao = f" ★ {reserva['avaliacao']}" if reserva.get("avaliacao") else ""
        print(f"{indice}. [{reserva['codigo']}] {reserva['nome']} — "
              f"{reserva.get('restaurante', 'N/A')} | {reserva['data']} {reserva['hora']} | "
              f"Mesa {reserva['mesa']} | {reserva['pessoas']} pax{avaliacao}")


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
        print(f"Código: {reserva['codigo']}, Nome: {reserva['nome']}, "
              f"Restaurante: {reserva['restaurante']}, Data: {reserva['data']}, "
              f"Hora: {reserva['hora']}, Pessoas: {reserva['pessoas']}, Mesa: {reserva['mesa']}")


def cancelar_reserva(reservas):
    if not reservas:
        print("\nNenhuma reserva encontrada.")
        return
    
    codigo = input("\nDigite o código da reserva que deseja cancelar: ").upper()

    for reserva in reservas:
        if reserva["codigo"] == codigo:
            reservas.remove(reserva)
            guardar_reservas(reservas)
            print(f"\nReserva {codigo} cancelada com sucesso!")
            
            return
        
    print("\nNenhuma reserva encontrada com esse código.")

#--------------------------------------------------
#                    MENU
#--------------------------------------------------
def mostrar_menu():
    print("\n======== P'a Comer ========")
    print("1. Adicionar reserva")
    print("2. Listar reservas")
    print("3. Pesquisar reserva")
    print("4. Cancelar reserva")
    print("5. Ver restaurantes")
    print("6. Avaliar restaurante")
    print("0. Sair")

def main():
    reservas = carregar_reservas()

    while True:
        mostrar_menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            adicionar_reserva(reservas)
        elif escolha == "2":
            listar_reservas(reservas)
        elif escolha == "3":
            pesquisar_reserva(reservas)
        elif escolha == "4":
            cancelar_reserva(reservas)
        elif escolha == "5":
            mostrar_restaurantes()
        elif escolha == "6":
            avaliar_restaurante(reservas)
        elif escolha == "0":
            print("\nObrigado por usar o \"P'a Comer\". Até breve!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()






