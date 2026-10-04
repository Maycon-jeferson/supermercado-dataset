from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


BASE_DIR = Path(__file__).resolve().parent.parent

CAMINHO_CSV = (
    BASE_DIR
    / "data"
    / "raw"
    / "SuperMarket Analysis.csv"
)


def criar_conexao():
    load_dotenv(BASE_DIR / ".env")

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    if not all([host, port, database, user, password]):
        raise ValueError(
            "As configurações do banco não foram encontradas no .env."
        )

    url = (
        f"postgresql+psycopg2://"
        f"{user}:{password}@{host}:{port}/{database}"
    )

    return create_engine(url)


def main():
    print("=" * 60)
    print("CARGA DA CAMADA RAW")
    print("=" * 60)

    print(f"\nArquivo: {CAMINHO_CSV}")

    # Leitura do CSV original
    df = pd.read_csv(CAMINHO_CSV)

    print(f"\nRegistros encontrados no CSV: {len(df)}")

    engine = criar_conexao()

    print("\nConectando ao PostgreSQL...")

    # Carrega os dados para a tabela Raw
    df.to_sql(
        "raw_vendas",
        con=engine,
        schema="public",
        if_exists="append",
        index=False,
    )

    print("Carga concluída.")

    # Validação da quantidade de registros
    with engine.connect() as conexao:
        resultado = conexao.execute(
            text("SELECT COUNT(*) FROM raw_vendas")
        )

        total_banco = resultado.scalar()

    print(f"\nRegistros no CSV:    {len(df)}")
    print(f"Registros no banco:  {total_banco}")

    if len(df) == total_banco:
        print("\nVALIDAÇÃO OK: CSV e PostgreSQL possuem a mesma quantidade.")
    else:
        print("\nERRO: quantidade de registros diferente.")


if __name__ == "__main__":
    main()