# ETL de Indicadores Econômicos

## Sobre o projeto

Este projeto consiste no desenvolvimento de um pipeline ETL (Extract, Transform, Load) para coleta, transformação e armazenamento de indicadores econômicos disponibilizados pelo Banco Central do Brasil (BCB).

Nesta primeira versão, foi utilizada a série histórica do IPCA mensal referente ao ano de 2025.

## Objetivo

Desenvolver um processo automatizado de Engenharia de Dados, aplicando conceitos de:

- Extração de dados via API REST;
- Transformação e tratamento de dados com Python;
- Armazenamento em banco de dados PostgreSQL;
- Execução integrada de um pipeline ETL;
- Testes automatizados com Pytest;
- Consultas SQL para análise dos dados.

## Tecnologias utilizadas

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Pytest
- API do Banco Central do Brasil (SGS)

## Arquitetura do projeto

O pipeline é composto por três etapas principais:

1. **Extract:** coleta os dados do IPCA por meio da API do Banco Central e salva os dados brutos em JSON.
2. **Transform:** realiza a conversão dos dados, ajustando os tipos das colunas e gerando um arquivo CSV.
3. **Load:** carrega os dados tratados em uma tabela PostgreSQL.

O arquivo `main.py` integra e executa todas as etapas do pipeline.

## Estrutura do projeto

```text
etl-indicadores-economicos/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── sql/
│   └── analise_ipca.sql
├── tests/
│   └── test_transform.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Configurar as variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=indicadores_economicos
DB_USER=postgres
DB_PASSWORD=sua_senha
```

### 6. Executar o pipeline

```bash
python src/main.py
```

## Testes automatizados

Para executar os testes:

```bash
python -m pytest -v
```

Os testes verificam a quantidade de registros, a existência das colunas esperadas, os tipos de dados e a ausência de valores nulos.

## Banco de dados

Os dados transformados são armazenados no PostgreSQL, na tabela `ipca`, no schema `public`.

O projeto também disponibiliza consultas SQL para análise dos indicadores.

## Fonte dos dados

Banco Central do Brasil — Sistema Gerenciador de Séries Temporais (SGS).

Série utilizada: IPCA mensal (código 433).

[API do Banco Central do Brasil](https://api.bcb.gov.br/)