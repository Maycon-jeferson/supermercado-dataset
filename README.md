# 📊 Projeto de Análise de Vendas

Projeto desenvolvido para a análise de dados de vendas de um supermercado, utilizando Python, Pandas, PostgreSQL e SQL.

O projeto aplica conceitos de **ETL, análise exploratória, estatística descritiva, consultas SQL e visualização de dados**, seguindo uma estrutura inspirada na arquitetura **Medallion**, com separação entre dados Raw, dados tratados e resultados analíticos.

---

## 🎯 Objetivo

Realizar o tratamento e a análise de um conjunto de dados de vendas de supermercado, respondendo perguntas de negócio relacionadas a:

* Receita por filial;
* Quantidade de vendas por filial;
* Receita por linha de produto;
* Avaliação média dos produtos;
* Formas de pagamento;
* Valor médio das vendas;
* Maior venda registrada;
* Vendas por dia da semana.

---

## 🗂️ Dataset

Foi utilizado o dataset **Supermarket Sales**, disponível no Kaggle.

**Fonte:** Kaggle — Supermarket Sales
**Autor:** faresashraf1001

O arquivo original foi preservado na camada Raw:

```text
data/raw/SuperMarket Analysis.csv
```

---

## 🛠️ Tecnologias utilizadas

* Python
* Pandas
* PostgreSQL
* SQL
* SQLAlchemy
* psycopg2
* python-dotenv
* Matplotlib
* Git
* GitHub

---

## 🏗️ Arquitetura do projeto

O projeto utiliza uma estrutura inspirada na arquitetura Medallion:

```text
Raw
 ↓
Tratamento / ETL
 ↓
Dados tratados
 ↓
Análise estatística
 ↓
Resultados
```

### Raw

Contém os dados originais, preservados sem alterações:

```text
data/raw/
```

Os dados também são carregados para a tabela PostgreSQL:

```text
raw_vendas
```

### Tratado

Os dados passam por limpeza, conversão de tipos e validações utilizando Pandas.

Resultado:

```text
data/processed/vendas_tratadas.csv
```

### Resultados

Contém os resultados das análises em CSV e os gráficos gerados:

```text
resultados/
├── *.csv
└── graficos/
```

---

## 📁 Estrutura do projeto

```text
projeto-analise-vendas/
│
├── data/
│   ├── raw/
│   │   └── SuperMarket Analysis.csv
│   │
│   └── processed/
│       └── vendas_tratadas.csv
│
├── resultados/
│   ├── receita_por_filial.csv
│   ├── quantidade_vendas_por_filial.csv
│   ├── receita_por_linha.csv
│   ├── avaliacao_por_produto.csv
│   ├── formas_pagamento.csv
│   ├── media_de_vendas.csv
│   ├── maior_venda.csv
│   ├── vendas_por_dia_da_semana.csv
│   │
│   └── graficos/
│       ├── 01_receita_por_filial.png
│       ├── 02_quantidade_vendas_por_filial.png
│       ├── 03_receita_por_linha.png
│       ├── 04_vendas_por_dia_da_semana.png
│       ├── 05_avaliacao_por_produto.png
│       ├── 06_formas_pagamento.png
│       ├── 07_media_de_vendas.png
│       └── 08_maior_venda.png
│
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_carga_raw.py
│   ├── 02_etl_vendas.py
│   └── 03_estatistica.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🔄 Processo de ETL

### 1. Leitura dos dados

O arquivo CSV original é carregado utilizando Pandas.

Foram realizadas verificações estruturais, incluindo:

* quantidade de linhas e colunas;
* tipos de dados;
* valores nulos;
* registros duplicados;
* unicidade do identificador da venda;
* estatísticas básicas.

O dataset possui:

* **1.000 registros**
* **17 colunas**
* **0 valores nulos**
* **0 registros duplicados**

### 2. Carga dos dados Raw

Os dados originais são carregados para o PostgreSQL na tabela:

```text
raw_vendas
```

A camada Raw mantém os dados originais para garantir rastreabilidade.

### 3. Tratamento dos dados

O processo de ETL realiza:

* renomeação das colunas;
* conversão de datas;
* conversão de horários;
* conversão dos campos numéricos;
* validação de valores nulos;
* validação de valores negativos;
* validação da quantidade;
* validação das avaliações;
* verificação de IDs duplicados;
* validação dos valores calculados.

O resultado é salvo em:

```text
data/processed/vendas_tratadas.csv
```

---

## 🗄️ Banco de dados

O projeto utiliza PostgreSQL.

Banco utilizado:

```text
supermercado
```

Tabela Raw:

```text
raw_vendas
```

A tabela possui:

* Primary Key;
* restrições `NOT NULL`;
* restrições `CHECK`;
* validação do identificador das vendas;
* validação de valores numéricos.

Exemplos de regras:

```sql
"Quantity" > 0
```

```sql
"Sales" >= 0
```

```sql
"Rating" >= 0 AND "Rating" <= 10
```

---

## 📈 Análises realizadas

### 1. Filial com maior receita

**Giza**

Receita total:

**R$ 110.568,71**

### 2. Filial com maior quantidade de vendas

**Alex**

Quantidade:

**340 vendas**

### 3. Linha de produto com maior receita

**Food and beverages**

Receita:

**R$ 56.144,84**

### 4. Linha de produto com melhor avaliação média

**Food and beverages**

Avaliação média:

**7,11**

### 5. Forma de pagamento mais utilizada

**Ewallet**

Quantidade:

**345 vendas**

### 6. Valor médio das vendas

**R$ 322,97**

### 7. Maior venda registrada

ID da venda:

```text
860-79-0874
```

Filial:

**Giza**

Linha de produto:

**Fashion accessories**

Valor:

**R$ 1.042,65**

### 8. Dia da semana com maior quantidade de vendas

**Sábado**

Quantidade:

**164 vendas**

---

## 📊 Visualizações

Foram gerados gráficos para auxiliar na interpretação dos resultados.

Os gráficos estão disponíveis em:

```text
resultados/graficos/
```

Entre eles:

* Receita por filial;
* Quantidade de vendas por filial;
* Receita por linha de produto;
* Vendas por dia da semana;
* Avaliação média por linha de produto;
* Formas de pagamento;
* Valor médio das vendas;
* Maior venda registrada.

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Maycon-jeferson/supermercado-dataset
cd projeto-analise-vendas
```

### 2. Criar o ambiente virtual

Windows:

```powershell
python -m venv .venv
```

Ativar:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

Criar o banco PostgreSQL utilizando:

```text
sql/01_criar_banco.sql
```

Depois criar a tabela:

```text
sql/02_criar_tabelas.sql
```

### 5. Configurar as credenciais

Criar um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=supermercado
DB_USER=postgres
DB_PASSWORD=SUA_SENHA
```

O arquivo `.env` não deve ser versionado.

### 6. Executar a leitura dos dados

```powershell
python src/01_leitura_dados.py
```

### 7. Carregar os dados Raw

```powershell
python src/02_carga_raw.py
```

### 8. Executar o ETL

```powershell
python src/02_etl_vendas.py
```

### 9. Executar as análises

```powershell
python src/03_estatistica.py
```

Os resultados serão salvos no diretório:

```text
resultados/
```

---

## 🔐 Segurança

Informações sensíveis, como credenciais do PostgreSQL, são armazenadas em `.env`.

O arquivo `.env` está incluído no `.gitignore` e não deve ser enviado para o GitHub.

O ambiente virtual `.venv` também é ignorado pelo Git.

---

## 📚 Organização do código

O projeto foi dividido em scripts com responsabilidades específicas:

| Arquivo                | Responsabilidade                        |
| ---------------------- | --------------------------------------- |
| `01_leitura_dados.py`  | Leitura e inspeção inicial do CSV       |
| `02_carga_raw.py`      | Carga dos dados originais no PostgreSQL |
| `02_etl_vendas.py`     | Tratamento e validação dos dados        |
| `03_estatistica.py`    | Estatísticas, análises e gráficos       |
| `01_criar_banco.sql`   | Criação do banco                        |
| `02_criar_tabelas.sql` | Criação e validação das tabelas         |
| `03_consultas.sql`     | Consultas SQL para análise              |


## 📌 Considerações finais

O projeto demonstra um fluxo completo de análise de dados, desde a leitura e preservação dos dados originais até o tratamento, armazenamento, análise estatística e apresentação dos resultados.

A separação das etapas permite maior organização, rastreabilidade e facilidade de reprodução do processo.
