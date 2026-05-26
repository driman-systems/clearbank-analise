import pandas as pd


LIMITE_SUSPEITO = 10000.00
CAMINHO_CSV = "transacoes.csv"


def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)


def limpar_dados(df):
    df_limpo = df.copy()

    df_limpo["id"] = pd.to_numeric(df_limpo["id"], errors="coerce")
    df_limpo["valor"] = pd.to_numeric(df_limpo["valor"], errors="coerce")
    df_limpo["data"] = pd.to_datetime(df_limpo["data"], format="%Y-%m-%d", errors="coerce")

    df_limpo["cliente_id"] = df_limpo["cliente_id"].astype(str).str.strip()
    df_limpo["tipo"] = df_limpo["tipo"].astype(str).str.strip().str.lower()

    df_limpo = df_limpo[
        df_limpo["id"].notna()
        & df_limpo["cliente_id"].notna()
        & (df_limpo["cliente_id"] != "")
        & (df_limpo["cliente_id"] != "nan")
        & df_limpo["data"].notna()
        & df_limpo["tipo"].isin(["credito", "debito"])
        & df_limpo["valor"].notna()
        & (df_limpo["valor"] > 0)
    ].copy()

    df_limpo["mes"] = df_limpo["data"].dt.strftime("%Y-%m")
    df_limpo["suspeita"] = df_limpo["valor"] > LIMITE_SUSPEITO

    return df_limpo


def gerar_resumo(df_limpo):
    resumo = df_limpo.groupby("mes").agg(
        quantidade=("id", "count"),
        total_credito=("valor", lambda x: x[df_limpo.loc[x.index, "tipo"] == "credito"].sum()),
        total_debito=("valor", lambda x: x[df_limpo.loc[x.index, "tipo"] == "debito"].sum()),
        media=("valor", "mean"),
        maior_valor=("valor", "max"),
        menor_valor=("valor", "min"),
    ).reset_index()

    resumo["saldo"] = resumo["total_credito"] - resumo["total_debito"]

    return resumo[
        [
            "mes",
            "quantidade",
            "total_credito",
            "total_debito",
            "saldo",
            "media",
            "maior_valor",
            "menor_valor",
        ]
    ]


def executar_analise_pandas():
    df = carregar_dados(CAMINHO_CSV)
    df_limpo = limpar_dados(df)
    resumo = gerar_resumo(df_limpo)

    print(resumo)
    return resumo


if __name__ == "__main__":
    executar_analise_pandas()
