
import pandas as pd
from pathlib import Path


def transform_ipca():

    # Localiza o arquivo JSON
    caminho = Path(__file__).resolve().parent.parent
    arquivo = caminho / "data" / "raw" / "ipca_2025.json"

    # Lê os dados brutos
    df = pd.read_json(arquivo)

    # Converte a coluna data para datetime
    df["data"] = pd.to_datetime(
        df["data"],
        format="%d/%m/%Y"
    )

    # Converte a coluna valor para numérico
    df["valor"] = pd.to_numeric(df["valor"])

    print("Transformação realizada com sucesso!")
    print(df)
    print("\nTipos de dados:")
    print(df.dtypes)

    # Salva os dados transformados
    arquivo_saida = caminho / "data" / "processed" / "ipca_2025.csv"
    arquivo_saida.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(arquivo_saida, index=False)
    print(f"Arquivo processado salvo em: {arquivo_saida}")

    return df

if __name__ == "__main__":
    transform_ipca()


