from pathlib import Path
import pandas as pd

# ============================================================
# CAMINHOS DO PROJETO
# ============================================================

# Define o diretório raiz subindo dois níveis a partir deste script
BASE_DIR = Path(__file__).resolve().parent.parent

# Aponta para o arquivo tratado gerado pelo script de ETL anterior
ARQUIVO_ENTRADA = (
    BASE_DIR
    / "data"
    / "processed"
    / "vendas_tratadas.csv"
)

# Diretório onde os artefatos da análise exploratória serão salvos
DIRETORIO_RESULTADOS = BASE_DIR / "resultados"

# ============================================================
# CARREGAMENTO
# ============================================================

def carregar_dados():
    """Carrega a base tratada para análise."""
    
    print("=" * 60)
    print("CARREGAMENTO DA BASE TRATADA")
    print("=" * 60)

    print(f"Arquivo: {ARQUIVO_ENTRADA}")

    # Lê o CSV tratado convertendo a coluna de data nativamente
    df = pd.read_csv(
        ARQUIVO_ENTRADA,
        parse_dates=["data_venda"]
    )

    print(f"Linhas carregadas: {len(df)}")
    print(f"Colunas carregadas: {len(df.columns)}")

    return df

# ============================================================
# ANÁLISE EXPLORATÓRIA
# ============================================================

def estatistica_descritiva(df):
    """Exibe estatísticas descritivas das variáveis numéricas."""

    print("\n" + "=" * 60)
    print("ESTATÍSTICA DESCRITIVA")
    print("=" * 60)

    colunas = [
        "preco_unitario",
        "Quantidade",
        "Imposto",
        "valor_total",
        "custo_mercadoria",
        "margem_percentual",
        "receita_bruta",
        "Avaliação"
    ]

    print(df[colunas].describe())

def analisar_receita_por_filial(df):
    """Calcula e exibe o faturamento total consolidado por filial."""
    
    print("\n" + "=" * 60)
    print("1. RECEITA POR FILIAL")
    print("=" * 60)

    resultado = (
        df.groupby("Filial")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    print(resultado)

    filial_maior_receita = resultado.idxmax()
    maior_receita = resultado.max()

    print(f"\nFilial com maior receita: {filial_maior_receita}")
    print(f"Receita: R$ {maior_receita:,.2f}")

    return resultado

def analisar_quantidade_vendas_por_filial(df):
    """Calcula o volume total de transações (vendas) por filial."""
    
    print("\n" + "=" * 60)
    print("2. QUANTIDADE DE VENDAS POR FILIAL")
    print("=" * 60)

    resultado = (
        df.groupby("Filial")
        .size()
        .sort_values(ascending=False)
    )

    print(resultado)

    filial_mais_vendas = resultado.idxmax()
    quantidade_vendas = resultado.max()

    print(f"\nFilial com mais vendas: {filial_mais_vendas}")
    print(f"Quantidade de vendas: {quantidade_vendas}")

    return resultado

def analisar_receita_por_linha_produto(df):
    """Calcula e exibe o faturamento total por linha de produto."""
    
    print("\n" + "=" * 60)
    print("3. RECEITA POR LINHA DE PRODUTO")
    print("=" * 60)

    resultado = (
        df.groupby("linha_produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    print(resultado)

    linha_maior_receita = resultado.idxmax()
    maior_receita = resultado.max()

    print(f"\nLinha de produto com maior receita: {linha_maior_receita}")
    print(f"Receita: R$ {maior_receita:,.2f}")

    return resultado

def analisar_avaliacao_por_linha_produto(df):
    """Calcula e exibe a nota média de satisfação dos clientes por linha de produto."""

    print("\n" + "=" * 60)
    print("4. AVALIAÇÃO MÉDIA POR LINHA DE PRODUTO")
    print("=" * 60)

    resultado = (
        df.groupby("linha_produto")["Avaliação"]
        .mean()
        .sort_values(ascending=False)
    )

    print(resultado)

    linha_melhor_avaliacao = resultado.idxmax()
    melhor_avaliacao = resultado.max()

    print(
        f"\nLinha de produto com melhor avaliação: "
        f"{linha_melhor_avaliacao}"
    )
    print(f"Avaliação média: {melhor_avaliacao:.2f}")

    return resultado

def analisar_forma_pagamento(df):
    """Calcula e exibe a frequência de uso de cada forma de pagamento."""
    
    print("\n" + "=" * 60)
    print("5. FORMAS DE PAGAMENTO")
    print("=" * 60)

    resultado = (
        df.groupby("forma_pagamento")
        .size()
        .sort_values(ascending=False)
    )

    print(resultado)

    forma_mais_utilizada = resultado.idxmax()
    quantidade = resultado.max()

    print(f"\nForma de pagamento mais utilizada: {forma_mais_utilizada}")
    print(f"Quantidade de vendas: {quantidade}")

    return resultado

def analisar_valor_medio_vendas(df):
    """Calcula e exibe o ticket médio (valor médio) das vendas."""
    
    print("\n" + "=" * 60)
    print("6. VALOR MÉDIO DAS VENDAS")
    print("=" * 60)

    valor_medio = df["valor_total"].mean()

    print(f"Valor médio de uma venda: R$ {valor_medio:,.2f}")

    # Retorna como um DataFrame formatado para facilitar a exportação para CSV
    return pd.DataFrame({
        "indicador": ["valor_medio_venda"],
        "valor": [valor_medio]
    })

def analisar_maior_venda(df):
    """Identifica e exibe os detalhes da transação de maior valor do dataset."""
    
    print("\n" + "=" * 60)
    print("7. MAIOR VENDA")
    print("=" * 60)

    indice_maior_venda = df["valor_total"].idxmax()
    maior_venda = df.loc[indice_maior_venda]

    print(f"ID da venda: {maior_venda['id_venda']}")
    print(f"Filial: {maior_venda['Filial']}")
    print(f"Linha de produto: {maior_venda['linha_produto']}")
    print(f"Valor da venda: R$ {maior_venda['valor_total']:,.2f}")

    # .to_frame().T converte a Series de volta em um DataFrame de uma única linha para exportação
    return maior_venda.to_frame().T

def analisar_vendas_por_dia_semana(df):
    """Calcula e exibe o volume de vendas por dia da semana."""
    
    print("\n" + "=" * 60)
    print("8. VENDAS POR DIA DA SEMANA")
    print("=" * 60)

    resultado = (
        df["data_venda"]
        .dt.day_name()
        .value_counts()
    )

    print(resultado)

    dia_mais_vendas = resultado.idxmax()
    quantidade_vendas = resultado.max()

    print(f"\nDia com mais vendas: {dia_mais_vendas}")
    print(f"Quantidade de vendas: {quantidade_vendas}")

    return resultado

# ============================================================
# EXPORTAÇÃO DE RESULTADOS
# ============================================================

def salvar_resultados(resultados):
    """Salva os resultados das análises em arquivos CSV separados."""

    # Cria a pasta 'resultados' caso não exista
    DIRETORIO_RESULTADOS.mkdir(parents=True, exist_ok=True)

    arquivos = {
        "receita_por_filial.csv": resultados["receita_por_filial"],
        "quantidade_vendas_por_filial.csv": resultados["quantidade_vendas_por_filial"],
        "receita_por_linha.csv": resultados["receita_por_linha"],
        "avaliacao_por_produto.csv": resultados["avaliacao_por_produto"],
        "formas_pagamento.csv": resultados["formas_pagamento"],
        "media_de_vendas.csv": resultados["media_de_vendas"],
        "maior_venda.csv": resultados["maior_venda"],
        "vendas_por_dia_da_semana.csv": resultados["vendas_por_dia_da_semana"],
    }

    print("\n" + "=" * 60)
    print("SALVANDO RESULTADOS")
    print("=" * 60)

    for nome_arquivo, resultado in arquivos.items():
        caminho = DIRETORIO_RESULTADOS / nome_arquivo

        # Salva o arquivo CSV mantendo o índice (importante, pois ele guarda nomes de filiais, produtos, etc.)
        resultado.to_csv(
            caminho,
            index=True,
            encoding="utf-8-sig"
        )

        print(f"Salvo: {caminho}")

# ============================================================
# MAIN
# ============================================================

def main():
    df = carregar_dados()

    estatistica_descritiva(df)

    # Dicionário que irá armazenar os dados gerados pelas funções
    resultados = {}

    resultados["receita_por_filial"] = analisar_receita_por_filial(df)
    
    resultados["quantidade_vendas_por_filial"] = analisar_quantidade_vendas_por_filial(df)
    
    resultados["receita_por_linha"] = analisar_receita_por_linha_produto(df)
    
    resultados["avaliacao_por_produto"] = analisar_avaliacao_por_linha_produto(df)
    
    resultados["formas_pagamento"] = analisar_forma_pagamento(df)
    
    resultados["media_de_vendas"] = analisar_valor_medio_vendas(df)
    
    resultados["maior_venda"] = analisar_maior_venda(df)
    
    resultados["vendas_por_dia_da_semana"] = analisar_vendas_por_dia_semana(df)

    # Função final que vai ler o dicionário e gravar tudo na pasta 'resultados'
    salvar_resultados(resultados)

if __name__ == "__main__":
    main()