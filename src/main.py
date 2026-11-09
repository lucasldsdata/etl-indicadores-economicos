from extract import extract_ipca
from transform import transform_ipca
from load import load_ipca


def main():

    print("Iniciando pipeline ETL...")

    # Etapa 1: Extração
    print("\nIniciando extração...")
    extract_ipca()

    # Etapa 2: Transformação
    print("\nIniciando transformação...")
    transform_ipca()

    # Etapa 3: Carga
    print("\nIniciando carga...")
    load_ipca()

    print("\nPipeline ETL executado com sucesso!")


if __name__ == "__main__":
    main()