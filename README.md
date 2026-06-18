# P'a Comer

> P'a Comer é uma app de reservas de restaurantes. Com o intuito de ajudar o cliente a reservar mesa em restaurantes, cancelar e poder avaliar o mesmo.



## Informação do Projeto

| Campo            | Detalhe                              |
|------------------|--------------------------------------|
| **Curso**        | UFCD 10790 – Projeto de Programação  |
| **Formando**     | Flávio Tavares Saldanha              |
| **Formador**     | Carlos Barata                        |
| **Instituição**  | IEFP                                 |
| **Data de início** | 01/06/2026                         |
| **Data de entrega** | 19/06/2026                        |
| **Versão**       | 1.0                                  |

---

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Como Instalar e Executar](#como-instalar-e-executar)
- [Base de Dados](#base-de-dados)
- [Arquitetura](#arquitetura)
- [Documentação](#documentação)
- [Estado do Projeto](#estado-do-projeto)

---

## Descrição

Explica aqui o projeto com um pouco mais de detalhe do que na frase de abertura.

- Qual o problema que resolve? - O intuito é ajudar os clientes dos restaurantes a poderem antever a sua mesa antes de chagar ao próprio local sem necessidade de o fazer pessoalmente ou por chamada. Prático, fácil e todos ficam a ganhar.
- Usuários da app; Admin
- Aplicação de consola em Python 

---

## Funcionalidades

Lista as principais funcionalidades implementadas:

 Funcionalidade 1 — Adicionar reserva com código único gerado automaticamente
 Funcionalidade 2 — Listar todas as reservas existentes
 Funcionalidade 3 — Pesquisar reserva por nome ou código
 Funcionalidade 4 — Cancelar reserva pelo código
 Funcionalidade 5 — Ver lista de restaurantes disponíveis com avaliação média
 Funcionalidade 6 — Avaliar restaurante com nota de 1 a 5 estrelas
 Funcionalidade 7 — Atribuição automática de mesa por disponibilidade

> As checkboxes ficam marcadas (`[x]`) à medida que implementas cada funcionalidade.

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

```

---

## Requisitos Técnicos

- Python 3.10 ou superior
- Bibliotecas necessárias (lista aqui as que usas):
  - `sqlite3` — incluído no Python (não precisa de instalação)
  - *(adiciona outras se necessário, ex: `bcrypt`, `tabulate`)*

Para instalar dependências externas (se houver):

```bash
pip install -r requirements.txt
```

---

## Como Instalar e Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/[teu-utilizador]/[nome-do-repositorio].git
cd [nome-do-repositorio]
```

### 2. (Opcional) Criar ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
cd src
python main.py
```

---

## Base de Dados

> Preenche esta secção se o projeto usa base de dados.

- **Sistema:** SQLite (ficheiro local) / *outro se aplicável*
- **Ficheiro:** `src/database.db` *(criado automaticamente na primeira execução)*
- **Esquema:** ver [`sql/criar_tabelas.sql`](sql/criar_tabelas.sql)

Para inicializar a base de dados manualmente a partir dos scripts SQL:

```bash
sqlite3 database.db < sql/criar_tabelas.sql
sqlite3 database.db < sql/dados_exemplo.sql
```

---

## Arquitetura

O projeto segue uma arquitetura em três camadas:

```
┌─────────────────────────────┐
│     UI — Interface          │  Interação com o utilizador
├─────────────────────────────┤
│     BLL — Lógica de Negócio │  Regras e validações
├─────────────────────────────┤
│     DAL — Acesso a Dados    │  Queries e persistência
├─────────────────────────────┤
│     Base de Dados           │  SQLite / outro
└─────────────────────────────┘
```

O diagrama completo está em [`assets/diagrama_arquitetura.png`](assets/diagrama_arquitetura.png).

---

## Documentação

| Documento                  | Localização                        | Descrição                              |
|----------------------------|------------------------------------|----------------------------------------|
| Relatório do Projeto       | `docs/relatorio.docx`              | Relatório completo do projeto          |
| Levantamento de Requisitos | `docs/requisitos.xlsx`             | Requisitos funcionais e não funcionais |
| Manual do Utilizador       | `docs/manual_utilizador.docx`      | Como usar a aplicação                  |
| Manual Técnico             | `docs/manual_tecnico.docx`         | Instalação e configuração              |
| Apresentação               | `assets/apresentacao.pptx`         | Slides da apresentação final           |

---

## Estado do Projeto

```
Sessão 1 — Requisitos        ✅ Concluído
Sessão 2 — Arquitetura       ✅ Concluído
Sessão 3 — Desenvolvimento 1 🔄 Em curso
Sessão 4 — Desenvolvimento 2 ⏳ Pendente
Sessão 5 — Apresentação      ⏳ Pendente
```

---

*UFCD 10790 – Projeto de Programação | [Ano letivo]*
