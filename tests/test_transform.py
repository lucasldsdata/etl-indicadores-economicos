from src.transform import transform_ipca

def test_transform_ipca():

    df = transform_ipca()

    # Verifica se existem 12 registros
    assert len(df) == 12

    # Verifica se as colunas esperadas existem
    assert "data" in df.columns
    assert "valor" in df.columns

    # Verifica os tipos de dados
    assert df["valor"].dtype == "float64"

    # Verifica se não existem valores vazios
    assert df["data"].notna().all()
    assert df["valor"].notna().all()