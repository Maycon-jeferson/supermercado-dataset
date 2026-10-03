from pathlib import Path

import pandas as pd


# Caminho do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho do dataset original
CAMINHO_CSV = BASE_DIR / "data" / "raw" / "SuperMarket Analysis.csv"


def main():
    print("=" * 60)
    print("LEITURA DO DATASET ORIGINAL")
    print("=" * 60)

    print(f"\nArquivo: {CAMINHO_CSV}")

    # Leitura do CSV original
    df = pd.read_csv(CAMINHO_CSV)

    print("\n--- Dimensões ---")
    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")

    print("\n--- Colunas ---")
    for coluna in df.columns:
        print(f"- {coluna}")

    print("\n--- Primeiras 5 linhas ---")
    print(df.head())

    print("\n--- Tipos de dados ---")
    print(df.dtypes)

    print("\n--- Valores nulos ---")
    print(df.isnull().sum())

    print("\n--- Linhas duplicadas ---")
    print(df.duplicated().sum())


    print("\n--- Informações gerais ---")
    df.info()

    print("\n--- Estatísticas descritivas ---")
    print(df.describe(include="all"))

if __name__ == "__main__":
    main()