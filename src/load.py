import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Localiza a raiz do projeto
caminho = Path(__file__).resolve().parent.parent

# Carrega as configurações do .env
load_dotenv(caminho / ".env")


# Configura os dados de conexão
host = os.getenv("DB_HOST")
porta = os.getenv("DB_PORT")
banco = os.getenv("DB_NAME")
usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")


# Cria a conexão com o PostgreSQL
engine = create_engine(
    f"postgresql+psycopg://{usuario}:{senha}@{host}:{porta}/{banco}"
)


def load_ipca():

    # Localiza o arquivo CSV
    arquivo = caminho / "data" / "processed" / "ipca_2025.csv"

    # Lê os dados transformados
    df = pd.read_csv(arquivo, parse_dates=["data"])

    # Carrega os dados no PostgreSQL
    df.to_sql(
        name="ipca",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Carga realizada com sucesso!")
    print(f"Registros carregados: {len(df)}")


if __name__ == "__main__":
    load_ipca()