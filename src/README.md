# P'a Comer — Documentação do Código

> Explicação completa do ficheiro `main.py` — como funciona, o que faz cada função e como os dados são guardados.

---

## Como correr o programa

```bash
python main.py
```

Não é necessário instalar nada. O Python já inclui todas as bibliotecas usadas.

---

## Bibliotecas utilizadas

```python
import json      # lê e escreve o ficheiro reservas.json
import os        # verifica se o ficheiro de dados existe
from datetime import datetime  # valida datas e horas
```

---

## Variáveis globais

```python
FICHEIRO_RESERVAS = "reservas.json"   # nome do ficheiro de dados
MESAS = [1, 2, 3, 4, 5, 6, 7, 8]     # lista de mesas disponíveis
RESTAURANTES = [...]                  # lista dos 5 restaurantes
```

`RESTAURANTES` é uma lista de dicionários. Cada restaurante tem:

| Campo             | Tipo  | Descrição                              |
|-------------------|-------|----------------------------------------|
| `id`              | int   | Identificador único                    |
| `nome`            | str   | Nome do restaurante                    |
| `cozinha`         | str   | Tipo de cozinha                        |
| `cidade`          | str   | Cidade onde está localizado            |
| `morada`          | str   | Endereço completo                      |
| `avaliacao_total` | int   | Soma de todas as notas recebidas       |
| `num_avaliacoes`  | int   | Número de avaliações feitas            |

---

## Estrutura de uma Reserva

Cada reserva é um dicionário Python guardado no ficheiro JSON:

```json
{
    "codigo": "R0001",
    "nome": "Flávio Saldanha",
    "data": "14-07-2026",
    "hora": "20:00",
    "pessoas": 4,
    "mesa": 3,
    "restaurante": "Tasca do Zé",
    "restaurante_id": 1,
    "avaliacao": null
}
```

| Campo            | Tipo     | Descrição                                        |
|------------------|----------|--------------------------------------------------|
| `codigo`         | str      | Código único gerado automaticamente (R0001…)     |
| `nome`           | str      | Nome do cliente                                  |
| `data`           | str      | Data da reserva no formato `dd-mm-aaaa`          |
| `hora`           | str      | Hora da reserva no formato `hh:mm`               |
| `pessoas`        | int      | Número de pessoas                                |
| `mesa`           | int      | Número da mesa atribuída automaticamente         |
| `restaurante`    | str      | Nome do restaurante                              |
| `restaurante_id` | int      | ID do restaurante — liga à lista `RESTAURANTES`  |
| `avaliacao`      | int/null | Nota de 1 a 5 — começa a `null` até ser avaliado |

---

## Funções — Resumo

| Função                     | O que faz                                                  |
|----------------------------|------------------------------------------------------------|
| `carregar_reservas()`      | Lê o ficheiro JSON e devolve a lista de reservas           |
| `guardar_reservas()`       | Escreve a lista de reservas no ficheiro JSON               |
| `obter_restaurante()`      | Devolve o dicionário de um restaurante pelo seu id         |
| `mostrar_restaurantes()`   | Imprime a lista de restaurantes com avaliação média        |
| `escolher_restaurante()`   | Pede ao utilizador que escolha um restaurante              |
| `avaliar_restaurante()`    | Regista uma nota de 1–5 numa reserva                       |
| `gerar_codigo_reserva()`   | Gera o próximo código sequencial (R0001, R0002…)           |
| `atribuir_mesas()`         | Encontra a primeira mesa livre no horário pretendido       |
| `criar_reserva()`          | Recolhe todos os dados e cria o dicionário da reserva      |
| `adicionar_reserva()`      | Adiciona a reserva à lista e guarda no ficheiro            |
| `listar_reservas()`        | Mostra todas as reservas no terminal                       |
| `pesquisar_reserva()`      | Pesquisa por nome do cliente ou código de reserva          |
| `cancelar_reserva()`       | Remove uma reserva da lista pelo código                    |
| `mostrar_menu()`           | Imprime as opções do menu no terminal                      |
| `main()`                   | Ponto de entrada — carrega dados e gere o ciclo principal  |

---

## Funções em Detalhe

---

### `carregar_reservas()`

Lê o ficheiro `reservas.json` e devolve a lista de reservas.
Se o ficheiro não existir (primeira vez que o programa corre), devolve uma lista vazia.

```python
def carregar_reservas():
    if os.path.exists(FICHEIRO_RESERVAS):
        with open(FICHEIRO_RESERVAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
```

---

### `guardar_reservas(reservas)`

Recebe a lista completa de reservas e escreve-a no ficheiro JSON.
É chamada sempre que há uma alteração — nova reserva, cancelamento ou avaliação.

```python
def guardar_reservas(reservas):
    with open(FICHEIRO_RESERVAS, "w", encoding="utf-8") as f:
        json.dump(reservas, f, indent=4, ensure_ascii=False)
```

---

### `obter_restaurante(restaurante_id)`

Percorre a lista `RESTAURANTES` e devolve o dicionário do restaurante com o id indicado.
Se não encontrar, devolve `None`.

```python
def obter_restaurante(restaurante_id):
    for restaurante in RESTAURANTES:
        if restaurante["id"] == int(restaurante_id):
            return restaurante
    return None
```

---

### `mostrar_restaurantes()`

Imprime a lista de restaurantes formatada em tabela.
Se o restaurante já tiver avaliações, calcula e mostra a média.

```python
def mostrar_restaurantes():
    for r in RESTAURANTES:
        if r["num_avaliacoes"] > 0:
            media = r["avaliacao_total"] / r["num_avaliacoes"]
            estrelas = f"  ★ {media:.1f}"
        else:
            estrelas = "  (sem avaliações)"
        print(f"  [{r['id']}]  {r['nome']:<26} {r['cozinha']:<14} {r['cidade']}{estrelas}")
```

---

### `escolher_restaurante()`

Mostra a lista de restaurantes e pede ao utilizador que escolha um pelo número.
Repete até o utilizador introduzir um número válido.

```python
def escolher_restaurante():
    mostrar_restaurantes()
    while True:
        try:
            escolha = int(input("  Escolha o número do restaurante: "))
            restaurante = obter_restaurante(escolha)
            if restaurante:
                return restaurante          # devolve o dicionário completo
            print("  Número inválido.")
        except ValueError:
            print("  Introduza um número válido.")
```

---

### `gerar_codigo_reserva(reservas)`

Conta as reservas existentes e gera o próximo código no formato `R0001`, `R0002`, etc.

```python
def gerar_codigo_reserva(reservas):
    numero = len(reservas) + 1
    return f"R{numero:04d}"    # :04d garante sempre 4 dígitos com zeros à esquerda
```

---

### `atribuir_mesas(reservas, data, hora, restaurante_id)`

Verifica quais mesas já estão ocupadas no mesmo restaurante, data e hora.
Devolve a primeira mesa livre. Se não houver nenhuma, devolve `None`.

```python
def atribuir_mesas(reservas, data, hora, restaurante_id):
    mesas_ocupadas = []
    for reserva in reservas:
        rid = reserva.get("restaurante_id")
        if rid is None:
            continue
        if (reserva["data"] == data
                and reserva["hora"] == hora
                and int(rid) == int(restaurante_id)):
            mesas_ocupadas.append(reserva["mesa"])
    for mesa in MESAS:
        if mesa not in mesas_ocupadas:
            return mesa
    return None
```

**Porquê o `rid = reserva.get("restaurante_id")`?**
O `.get()` é mais seguro que `reserva["restaurante_id"]` — se o campo não existir numa reserva antiga, devolve `None` em vez de dar erro.

---

### `criar_reserva(reservas)`

Guia o utilizador por todos os passos para criar uma reserva:
escolha do restaurante → nome → data → hora → pessoas → verificação de disponibilidade.

Pontos importantes:
- A data é validada com `datetime.strptime()` — rejeita formatos inválidos e datas no passado
- O `hoje` é definido **antes** do ciclo `while` para estar sempre disponível
- O número de pessoas tem validação — aceita apenas inteiros positivos
- Se não houver mesa disponível, termina sem criar a reserva

```python
return {
    "codigo":         codigo_reserva,
    "nome":           nome,
    "data":           data,
    "hora":           hora,
    "pessoas":        pessoas,
    "mesa":           mesa,
    "restaurante_id": restaurante["id"],
    "restaurante":    restaurante["nome"],
    "avaliacao":      None                # começa sem avaliação
}
```

---

### `adicionar_reserva(reservas)`

Chama `criar_reserva()` e, se a reserva foi criada com sucesso, adiciona-a à lista e guarda no ficheiro.

```python
def adicionar_reserva(reservas):
    reserva = criar_reserva(reservas)
    if reserva is not None:
        reservas.append(reserva)
        guardar_reservas(reservas)
```

---

### `listar_reservas(reservas)`

Mostra todas as reservas numa tabela formatada.
Usa `.get("avaliacao")` para evitar erros em reservas sem esse campo.

---

### `pesquisar_reserva(reservas)`

Pesquisa por nome (parcial) ou código (exato).
Converte tudo para minúsculas com `.lower()` para que a pesquisa seja insensível a maiúsculas.

```python
pesquisa = input(...).lower()
if pesquisa in reserva["nome"].lower() or pesquisa == reserva["codigo"].lower():
```

---

### `cancelar_reserva(reservas)`

Remove a reserva da lista com `.remove()` e guarda o ficheiro atualizado.
A reserva é apagada definitivamente — não fica como cancelada, desaparece da lista.

---

### `avaliar_restaurante(reservas)`

Permite dar uma nota de 1 a 5 estrelas a uma reserva pelo seu código.

Proteções implementadas:
- Impede avaliar se não há reservas
- Impede avaliar uma reserva que não existe
- Impede avaliar duas vezes (verifica se `avaliacao` já tem valor)
- Valida que a nota está entre 1 e 5

Após guardar a nota na reserva, atualiza também os totais do restaurante em memória:

```python
r["avaliacao_total"] += nota
r["num_avaliacoes"] += 1
media = r["avaliacao_total"] / r["num_avaliacoes"]
```

---

### `main()`

Ponto de entrada do programa. Carrega as reservas do ficheiro e entra num ciclo de menu.

```python
def main():
    reservas = carregar_reservas()    # carrega dados ao iniciar
    while True:                        # ciclo infinito até escolher 0
        mostrar_menu()
        escolha = input(...).strip()
        if escolha == "1":
            adicionar_reserva(reservas)
        ...
        elif escolha == "0":
            break                      # termina o programa
```

```python
if __name__ == "__main__":
    main()
```

Esta condição garante que `main()` só é chamada quando o ficheiro é executado diretamente — não quando é importado por outro script.

---

## Fluxo de dados

```
Utilizador
    │
    ▼
main()
    │
    ├── adicionar_reserva()
    │       ├── escolher_restaurante()  ──→  obter_restaurante()
    │       ├── criar_reserva()         ──→  atribuir_mesas()
    │       │                           ──→  gerar_codigo_reserva()
    │       └── guardar_reservas()      ──→  reservas.json
    │
    ├── listar_reservas()      ──→  carregar_reservas()
    ├── pesquisar_reserva()    ──→  carregar_reservas()
    ├── cancelar_reserva()     ──→  guardar_reservas()
    ├── mostrar_restaurantes() ──→  RESTAURANTES (memória)
    └── avaliar_restaurante()  ──→  guardar_reservas()
```

---

## Erros comuns e soluções

| Erro | Causa | Solução |
|------|-------|---------|
| `KeyError: 'restaurante'` | Reserva antiga no JSON sem o campo | Apagar `reservas.json` |
| `TypeError: string indices must be integers` | `restaurante_id` guardado como string | Usar `int(rid) == int(restaurante_id)` |
| `NameError: name 'Mesas' is not defined` | Nome da variável errado | Usar `MESAS` (tudo maiúsculas) |
| `TypeError: enconding` | Erro de digitação no argumento | Usar `encoding` (não `enconding`) |

---

*Flávio Saldanha · UFCD 10790 · 2026*
