# P'a Comer

> P'a Comer é uma aplicação de reservas em restaurantes. Permite ao cliente reservar uma mesa, consultar, cancelar e avaliar o restaurante — tudo a partir do terminal, sem necessidade de deslocação ou chamada.

## Informação do Projeto

| Campo               | Detalhe                             |
| ------------------- | ----------------------------------- |
| **Curso**           | UFCD 10790 – Projeto de Programação |
| **Formando**        | Flávio Tavares Saldanha             |
| **Formador**        | Carlos Barata                       |
| **Instituição**     | IEFP                                |
| **Data de início**  | 01/06/2026                          |
| **Data de entrega** | 19/06/2026                          |
| **Versão**          | 1.0                                 |

---

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Como Instalar e Executar](#como-instalar-e-executar)
- [Dados](#dados)
- [Arquitetura](#arquitetura)
- [Documentação](#documentação)
- [Estado do Projeto](#estado-do-projeto)

---

## Descrição

**P'a Comer** é uma aplicação de consola desenvolvida em Python que simula uma plataforma de reservas em restaurantes.

- **Problema que resolve:** Permite ao cliente reservar uma mesa antecipadamente, sem necessidade de se deslocar ao restaurante ou fazer uma chamada. Prático, rápido e acessível.
- **Utilizadores:** Cliente final (via terminal)
- **Tecnologia:** Python puro — sem frameworks ou bibliotecas externas
- **Persistência:** Ficheiro `reservas.json` criado automaticamente na primeira execução

---

## Funcionalidades

- [x] Funcionalidade 1 — Adicionar reserva com código único gerado automaticamente
- [x] Funcionalidade 2 — Listar todas as reservas existentes
- [x] Funcionalidade 3 — Pesquisar reserva por nome ou código
- [x] Funcionalidade 4 — Cancelar reserva pelo código
- [x] Funcionalidade 5 — Ver lista de restaurantes disponíveis com avaliação média
- [x] Funcionalidade 6 — Avaliar restaurante com nota de 1 a 5 estrelas
- [x] Funcionalidade 7 — Atribuição automática de mesa por disponibilidade

---

## Estrutura do Repositório

```
projeto-ufcd-10790/
│
├── README.md                   ← Este ficheiro — apresentação do projeto
├── .gitignore                  ← Ficheiros a ignorar pelo Git
├── reservas.json               ← Dados das reservas (gerado automaticamente)
│
├── src/                        ← Código fonte Python
│   └── main.py                 ← Ponto de entrada da aplicação (ficheiro único)
│
├── docs/                       ← Documentação do projeto
│   ├── relatorio.pdf           ← Relatório final do projeto
│   └── explicacao_codigo.docx  ← Explicação linha a linha do código
│
├── assets/                     ← Recursos visuais e apresentação
│   ├── apresentacao.pptx       ← Apresentação final
│   └── gantt.xlsx              ← Diagrama de Gantt do projeto
│
```

---

## Requisitos Técnicos

- Python 3.10 ou superior
- Sem bibliotecas externas — apenas módulos nativos do Python:
  - `json` — leitura e escrita do ficheiro de dados
  - `os` — verificação da existência do ficheiro
  - `datetime` — validação de datas e horas
  - `random` + `string` — geração de códigos únicos de reserva

Não é necessário instalar nada. Basta ter o Python instalado.

---

## Como Instalar e Executar

### 1. Clonar o repositório

```
git clone https://github.com/16bitsvnm66/projeto-ufcd-10790.git
cd projeto-ufcd-10790
```

### 2. Executar a aplicação

```
cd src
python main.py
```

O ficheiro `reservas.json` é criado automaticamente na primeira reserva.

---

## Dados

- **Formato:** JSON (ficheiro local `reservas.json`)
- **Criação:** Automática na primeira execução
- **Estrutura de uma reserva:**

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

### Restaurantes disponíveis

| ID | Nome                  | Cozinha    | Cidade  |
|----|-----------------------|------------|---------|
| 1  | Tasca do Zé           | Portuguesa | Lisboa  |
| 2  | Marisqueira Atlântico | Mariscos   | Cascais |
| 3  | Sushi Nagoya          | Japonesa   | Lisboa  |
| 4  | La Piazza             | Italiana   | Porto   |
| 5  | Adega Alentejana      | Alentejana | Évora   |

---

## Arquitetura

O projeto é uma aplicação de camada única — todo o código está em `main.py`, organizado em funções com responsabilidades bem definidas:

```
┌─────────────────────────────────────┐
│         UI — Menu Terminal          │  mostrar_menu(), main()
├─────────────────────────────────────┤
│      Lógica de Negócio              │  criar_reserva(), atribuir_mesas()
│                                     │  avaliar_restaurante(), pesquisar_reserva()
├─────────────────────────────────────┤
│      Persistência de Dados          │  carregar_reservas(), guardar_reservas()
├─────────────────────────────────────┤
│      Ficheiro JSON                  │  reservas.json
└─────────────────────────────────────┘
```

### Fluxo de uma reserva

```
Utilizador
    │
    ▼
escolher_restaurante()
    │
    ▼
criar_reserva()  ──→  atribuir_mesas()  ──→  gerar_codigo_reserva()
    │
    ▼
adicionar_reserva()  ──→  guardar_reservas()  ──→  reservas.json
```

---

## Documentação

| Documento             | Localização                    | Descrição                            |
| --------------------- | ------------------------------ | ------------------------------------ |
| Relatório do Projeto  | `docs/relatorio.pdf`           | Relatório completo do projeto        |
| Explicação do Código  | `docs/explicacao_codigo.docx`  | Explicação linha a linha de cada função |
| Apresentação          | `assets/apresentacao.pptx`     | Slides da apresentação final         |
| Diagrama de Gantt     | `assets/gantt.xlsx`            | Planeamento e fases do projeto       |

---

## Estado do Projeto

```
Análise e Planeamento    ✅ Concluído
Desenvolvimento          ✅ Concluído
Testes e Correções       ✅ Concluído
Documentação             ✅ Concluído
Apresentação             ⏳ Pendente
```

---

*UFCD 10790 – Projeto de Programação | 2026*
