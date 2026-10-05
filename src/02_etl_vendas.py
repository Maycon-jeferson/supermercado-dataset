from pathlib import Path
import pandas as pd

# ============================================================
# CAMINHOS DO PROJETO
# ============================================================

# Define o diretório raiz do projeto subindo dois níveis a partir deste script.
# Isso garante que os caminhos funcionem em qualquer computador ou sistema operacional.
BASE_DIR = Path(__file__).resolve().parent.parent

# Constrói o caminho completo para o arquivo bruto (input)
ARQUIVO_ENTRADA = (
    BASE_DIR
    / "data"
    / "raw"
    / "SuperMarket Analysis.csv"
)

# Constrói o caminho completo para o arquivo tratado (output)
ARQUIVO_SAIDA = (
    BASE_DIR
    / "data"
    / "processed"
    / "vendas_tratadas.csv"
)

# ============================================================
# CARREGAMENTO
# ============================================================

def carregar_dados():
    """Carrega o arquivo CSV original."""

    print("=" * 60)
    print("CARREGAMENTO DOS DADOS")
    print("=" * 60)

    print(f"Arquivo: {ARQUIVO_ENTRADA}")

    # Lê o arquivo CSV e o converte em um DataFrame (tabela) do Pandas
    df = pd.read_csv(ARQUIVO_ENTRADA)

    # Exibe a volumetria inicial para conferência
    print(f"Linhas carregadas: {len(df)}")
    print(f"Colunas carregadas: {len(df.columns)}")

    return df

# ============================================================
# INSPEÇÃO
# ============================================================

def inspecionar_dados(df):
    """Realiza uma inspeção inicial dos dados."""

    print("\n" + "=" * 60)
    print("INSPEÇÃO DOS DADOS")
    print("=" * 60)

    print("\nColunas:")
    print(df.columns.tolist())

    print("\nTipos de dados:")
    # Mostra se o Pandas interpretou as colunas como texto (object), número (int/float) ou data (datetime)
    print(df.dtypes)

    print("\nValores nulos:")
    # Retorna a soma de valores nulos (vazios) encontrados em cada coluna
    print(df.isnull().sum())

    # Verifica quantas linhas são duplicatas exatas de outras linhas na base
    print(f"\nDuplicatas: {df.duplicated().sum()}")

# ============================================================
# TRANSFORMAÇÃO
# ============================================================

def transformar_dados(df):
    """Limpa e transforma os dados para a camada tratada."""

    # Cria uma cópia na memória para evitar o aviso de 'SettingWithCopyWarning' do Pandas
    # e garantir que não estamos alterando a referência original por acidente
    df = df.copy()

    print("\n" + "=" * 60)
    print("TRANSFORMAÇÃO DOS DADOS")
    print("=" * 60)

    # --------------------------------------------------------
    # Padronização dos nomes das colunas
    # --------------------------------------------------------
    
    # Renomeia as colunas de inglês para português e as deixa mais descritivas
    df = df.rename(columns={
        "Invoice ID": "id_venda",
        "Branch": "Filial",
        "City": "Cidade",
        "Customer type": "tipo_cliente",
        "Gender": "Gênero",
        "Product line": "linha_produto",
        "Unit price": "preco_unitario",
        "Quantity": "Quantidade",
        "Tax 5%": "Imposto",
        "Sales": "valor_total",
        "Date": "data_venda",
        "Time": "hora_venda",
        "Payment": "forma_pagamento",
        "cogs": "custo_mercadoria",
        "gross margin percentage": "margem_percentual",
        "gross income": "receita_bruta",
        "Rating": "Avaliação"
    })

    # --------------------------------------------------------
    # Conversão de data
    # --------------------------------------------------------

    # O parâmetro errors="coerce" força valores de data mal formatados a virarem 'NaT' (Not a Time),
    # impedindo que o script quebre por causa de um único erro de digitação na base.
    df["data_venda"] = pd.to_datetime(
        df["data_venda"],
        errors="coerce"
    )

    # --------------------------------------------------------
    # Conversão de hora
    # --------------------------------------------------------

    # .str.strip() remove espaços acidentais no início/fim da string.
    # format="%I:%M:%S %p" avisa ao Pandas que a hora está no formato 12h (AM/PM).
    # .dt.time extrai apenas a parte da hora (ignorando data).
    df["hora_venda"] = pd.to_datetime(
        df["hora_venda"].str.strip(),
        format="%I:%M:%S %p"
    ).dt.time

    # --------------------------------------------------------
    # Conversão das colunas numéricas
    # --------------------------------------------------------

    colunas_numericas = [
        "preco_unitario",
        "Quantidade",
        "Imposto",
        "valor_total",
        "custo_mercadoria",
        "margem_percentual",
        "receita_bruta",
        "Avaliação"
    ]

    # Garante que todas essas colunas sejam de fato números,
    # convertendo textos acidentais em 'NaN' (Not a Number) devido ao "coerce".
    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        )

    # --------------------------------------------------------
    # Verificação após transformação
    # --------------------------------------------------------

    print("\nNulos após transformação:")
    # Filtra e exibe apenas as colunas que acabaram gerando algum valor nulo na transformação
    print(
        df.isnull().sum()
        [df.isnull().sum() > 0]
    )

    return df

# ============================================================
# SALVAMENTO
# ============================================================

def salvar_dados(df):
    """Salva os dados tratados em CSV."""

    # Cria toda a árvore de diretórios (como /data/processed/) caso não existam.
    # O exist_ok=True evita erro se a pasta já estiver criada.
    ARQUIVO_SAIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Salva sem o índice do Pandas (index=False) para não criar uma coluna de numeração extra.
    # O encoding 'utf-8-sig' é excelente pois força o Excel a reconhecer os acentos corretamente.
    df.to_csv(
        ARQUIVO_SAIDA,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n" + "=" * 60)
    print("DADOS SALVOS")
    print("=" * 60)

    print(f"Arquivo: {ARQUIVO_SAIDA}")
    print(f"Linhas: {len(df)}")
    print(f"Colunas: {len(df.columns)}")

# ============================================================
# VALIDAÇÃO
# ============================================================

def validar_dados(df):
    """Valida regras lógicas e limites de negócios na base tratada."""

    print("\n" + "=" * 60)
    print("VALIDAÇÃO DOS DADOS")
    print("=" * 60)

    print("\nQuantidade de registros:", len(df))
    # Conta quantos IDs únicos existem para verificar se não há cupons fiscais faturados duas vezes
    print("Quantidade de IDs únicos:", df["id_venda"].nunique())

    print("\nValores negativos:")

    colunas_nao_negativas = [
        "preco_unitario",
        "Imposto",
        "valor_total",
        "custo_mercadoria",
        "receita_bruta"
    ]

    # Varre colunas financeiras e conta quantas vezes ocorre um valor abaixo de 0 (o que indicaria erro na base)
    for coluna in colunas_nao_negativas:
        quantidade = (df[coluna] < 0).sum()
        print(f"{coluna}: {quantidade}")

    print("\nQuantidades inválidas:")
    # Vendas precisam ter pelo menos 1 item vendido
    print((df["Quantidade"] <= 0).sum())

    print("\nAvaliações fora do intervalo 0-10:")
    # Avalia os limites da nota de satisfação do cliente
    print(
        (
            (df["Avaliação"] < 0)
            | (df["Avaliação"] > 10)
        ).sum()
    )

    print("\nIDs duplicados:")
    # Verifica se algum 'id_venda' se repete, o que pode indicar problemas de duplicação
    print(df["id_venda"].duplicated().sum())

def validar_calculos(df):
    """Valida a consistência matemática dos valores considerando as regras do negócio."""

    print("\n" + "=" * 60)
    print("VALIDAÇÃO DOS CÁLCULOS")
    print("=" * 60)

    # Custo da mercadoria (Cogs = Preço unitário x Quantidade)
    custo_calculado = (
        df["preco_unitario"] * df["Quantidade"]
    )

    # Usa .abs() para ignorar o sinal negativo caso o original seja maior que o calculado
    diferenca_custo = (
        custo_calculado - df["custo_mercadoria"]
    ).abs()

    # Consideramos uma divergência apenas se for maior que 0.01 (1 centavo) 
    # para evitar falsos positivos causados por problemas de arredondamento de casas decimais.
    print(
        "\nDiferenças em preco_unitario x Quantidade:",
        (diferenca_custo > 0.01).sum()
    )

    # Imposto (Definido como 5% do custo da mercadoria)
    imposto_calculado = (
        df["custo_mercadoria"] * 0.05
    )

    diferenca_imposto = (
        imposto_calculado - df["Imposto"]
    ).abs()

    print(
        "Diferenças no imposto de 5%:",
        (diferenca_imposto > 0.01).sum()
    )

    # Valor total (Custo da mercadoria + Impostos)
    valor_calculado = (
        df["custo_mercadoria"] + df["Imposto"]
    )

    diferenca_total = (
        valor_calculado - df["valor_total"]
    ).abs()

    print(
        "Diferenças no valor total:",
        (diferenca_total > 0.01).sum()
    )

    # Receita bruta (Neste dataset, a margem de lucro bruto equivale fixamente a 5% do custo)
    receita_calculada = (
        df["custo_mercadoria"] * 0.05
    )

    diferenca_receita = (
        receita_calculada - df["receita_bruta"]
    ).abs()

    print(
        "Diferenças na receita bruta:",
        (diferenca_receita > 0.01).sum()
    )

# ============================================================
# MAIN
# ============================================================

def main():
    # Orquestra a execução de todo o pipeline seguindo a ordem lógica: 
    # Extrair -> Inspecionar -> Transformar -> Validar -> Carregar (Salvar)

    df = carregar_dados()

    inspecionar_dados(df)

    df = transformar_dados(df)

    print("\n" + "=" * 60)
    print("DADOS TRANSFORMADOS")
    print("=" * 60)

    print("\nColunas:")
    print(df.columns.tolist())

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nPrimeiras 5 linhas:")
    # Mostra uma amostra visual do início da tabela para conferência
    print(df.head())

    # Chamada das validações de negócio e regras lógicas
    validar_dados(df)
    validar_calculos(df)

    # Exportação final do dado tratado
    salvar_dados(df)

# Bloqueio padrão do Python que impede que a função main() seja executada automaticamente 
# caso este script seja importado por outro arquivo em vez de rodado diretamente.
if __name__ == "__main__":
    main()