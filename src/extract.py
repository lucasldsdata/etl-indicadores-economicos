
import requests
import json
from pathlib import Path


def extract_ipca():

    """
    Extrai os dados do IPCA da API do Banco Central.
    """

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados"

    params = {
        "formato": "json",
        "dataInicial": "01/01/2025",
        "dataFinal": "31/12/2025"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    dados = response.json()

    if not dados:
        print("Nenhum dado foi retornado pela API.")
        return []

    # Caminho da pasta de dados brutos
    caminho = Path(__file__).resolve().parent.parent / "data" / "raw"

    # Cria a pasta caso ela não exista
    caminho.mkdir(parents=True, exist_ok=True)

    # Salva os dados em JSON
    arquivo = caminho / "ipca_2025.json"

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print("Extração realizada com sucesso!")
    print(f"Quantidade de registros: {len(dados)}")
    print(f"Arquivo salvo em: {arquivo}")

    return dados


if __name__ == "__main__":
    extract_ipca()
