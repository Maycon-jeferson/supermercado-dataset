from pathlib import Path
import matplotlib.pyplot as plt
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

# Diretório onde os artefatos em CSV serão salvos
DIRETORIO_RESULTADOS = BASE_DIR / "resultados"

# Diretório onde as imagens dos gráficos serão salvas
DIRETORIO_GRAFICOS = DIRETORIO_RESULTADOS / "graficos"

# ============================================================
# CARREGAMENTO
# ============================================================

def carregar_dados():
    """Carrega a base tratada para análise."""
    
    print("=" * 60)
    print("CARREGAMENTO DA BASE TRATADA")
    print("=" * 60)

    print(f"Arquivo: {ARQUIVO_ENTRADA}")

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
# EXPORTAÇÃO E VISUALIZAÇÃO
# ============================================================

def salvar_resultados(resultados):
    """Salva os resultados das análises em arquivos CSV separados."""

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

        resultado.to_csv(
            caminho,
            index=True,
            encoding="utf-8-sig"
        )

        print(f"Salvo: {caminho}")

def gerar_graficos(resultados):
    """Gera os gráficos das principais análises."""

    DIRETORIO_GRAFICOS.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 60)
    print("GERANDO GRÁFICOS")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. Receita por filial
    # --------------------------------------------------------
    receita_filial = resultados["receita_por_filial"]
    plt.figure(figsize=(8, 5))
    receita_filial.plot(kind="bar")
    plt.title("Receita Total por Filial")
    plt.xlabel("Filial")
    plt.ylabel("Receita (R$)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "01_receita_por_filial.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 2. Quantidade de vendas por filial
    # --------------------------------------------------------
    quantidade_filial = resultados["quantidade_vendas_por_filial"]
    plt.figure(figsize=(8, 5))
    quantidade_filial.plot(kind="bar")
    plt.title("Quantidade de Vendas por Filial")
    plt.xlabel("Filial")
    plt.ylabel("Quantidade de vendas")
    plt.xticks(rotation=0)
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "02_quantidade_vendas_por_filial.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 3. Receita por linha de produto
    # --------------------------------------------------------
    receita_produto = resultados["receita_por_linha"]
    plt.figure(figsize=(10, 6))
    receita_produto.sort_values().plot(kind="barh")
    plt.title("Receita por Linha de Produto")
    plt.xlabel("Receita (R$)")
    plt.ylabel("Linha de produto")
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "03_receita_por_linha.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 4. Vendas por dia da semana
    # --------------------------------------------------------
    vendas_dia = resultados["vendas_por_dia_da_semana"]
    ordem_dias = [
        "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"
    ]
    vendas_dia = vendas_dia.reindex(ordem_dias)
    
    plt.figure(figsize=(10, 5))
    vendas_dia.plot(kind="bar")
    plt.title("Quantidade de Vendas por Dia da Semana")
    plt.xlabel("Dia da semana")
    plt.ylabel("Quantidade de vendas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "04_vendas_por_dia_da_semana.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 5. Avaliação média por linha de produto
    # --------------------------------------------------------
    avaliacao_produto = resultados["avaliacao_por_produto"]
    plt.figure(figsize=(10, 6))
    # Ordena para a maior nota ficar no topo
    avaliacao_produto.sort_values().plot(kind="barh", color="#17a2b8")
    plt.title("Avaliação Média por Linha de Produto")
    plt.xlabel("Avaliação (0 a 10)")
    plt.ylabel("Linha de produto")
    plt.xlim(0, 10) # Trava o eixo X no máximo da nota (10)
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "05_avaliacao_por_produto.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 6. Formas de pagamento
    # --------------------------------------------------------
    formas_pagamento = resultados["formas_pagamento"]
    plt.figure(figsize=(8, 8))
    # Um gráfico de pizza é excelente para mostrar proporções/fatias do todo
    formas_pagamento.plot(kind="pie", autopct="%1.1f%%", startangle=90, cmap="Pastel1")
    plt.title("Distribuição das Formas de Pagamento")
    plt.ylabel("") # Remove o título lateral que o Pandas coloca por padrão na pizza
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "06_formas_pagamento.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 7. Média de Vendas (Ticket Médio - KPI Card)
    # --------------------------------------------------------
    # Extrai o valor do DataFrame retornado pela função
    media_vendas = resultados["media_de_vendas"]["valor"].iloc[0]
    
    plt.figure(figsize=(6, 4))
    plt.axis("off") # Esconde os eixos, deixando apenas o texto
    plt.text(
        0.5, 0.5, 
        f"Ticket Médio:\nR$ {media_vendas:,.2f}", 
        fontsize=24, ha="center", va="center", fontweight="bold", color="#28a745"
    )
    plt.title("Indicador de Desempenho", fontsize=14, color="gray")
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "07_media_de_vendas.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

    # --------------------------------------------------------
    # 8. Maior Venda (KPI Card)
    # --------------------------------------------------------
    maior_venda = resultados["maior_venda"].iloc[0]
    
    plt.figure(figsize=(8, 4))
    plt.axis("off") # Esconde os eixos
    
    # Monta o texto que vai dentro do quadro
    texto_card = (
    f"MAIOR VENDA REGISTRADA\n\n"
    f"ID da Venda: {maior_venda['id_venda']}\n"
    f"Filial: {maior_venda['Filial']}\n"
    f"Produto: {maior_venda['linha_produto']}\n\n"
    f"Valor Total: R$ {maior_venda['valor_total']:,.2f}"
)
    
    # Renderiza o texto com uma caixa (bbox) em volta simulando um cartão
    plt.text(
        0.5, 0.5, texto_card, 
        fontsize=14, ha="center", va="center", 
        bbox=dict(facecolor="#f8f9fa", edgecolor="#ced4da", boxstyle="round,pad=1")
    )
    plt.tight_layout()
    caminho = DIRETORIO_GRAFICOS / "08_maior_venda.png"
    plt.savefig(caminho, dpi=300)
    plt.close()
    print(f"Salvo: {caminho}")

# ============================================================
# MAIN
# ============================================================

def main():
    df = carregar_dados()

    estatistica_descritiva(df)

    resultados = {}

    resultados["receita_por_filial"] = analisar_receita_por_filial(df)
    resultados["quantidade_vendas_por_filial"] = analisar_quantidade_vendas_por_filial(df)
    resultados["receita_por_linha"] = analisar_receita_por_linha_produto(df)
    resultados["avaliacao_por_produto"] = analisar_avaliacao_por_linha_produto(df)
    resultados["formas_pagamento"] = analisar_forma_pagamento(df)
    resultados["media_de_vendas"] = analisar_valor_medio_vendas(df)
    resultados["maior_venda"] = analisar_maior_venda(df)
    resultados["vendas_por_dia_da_semana"] = analisar_vendas_por_dia_semana(df)

    salvar_resultados(resultados)
    gerar_graficos(resultados)

if __name__ == "__main__":
    main()