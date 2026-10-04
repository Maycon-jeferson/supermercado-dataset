-- ============================================================
-- Projeto: Análise de Dados com Python
-- Etapa: Criação das tabelas
-- Camada: Raw
-- ============================================================

-- Cria Tabelas
CREATE TABLE IF NOT EXISTS raw_vendas (
    "Invoice ID" VARCHAR(50) PRIMARY KEY,
    "Branch" VARCHAR(10) NOT NULL,
    "City" VARCHAR(100) NOT NULL,
    "Customer type" VARCHAR(50) NOT NULL,
    "Gender" VARCHAR(20) NOT NULL,
    "Product line" VARCHAR(150) NOT NULL,
    "Unit price" NUMERIC(10, 2) NOT NULL,
    "Quantity" INTEGER NOT NULL,
    "Tax 5%" NUMERIC(10, 2) NOT NULL,
    "Sales" NUMERIC(12, 2) NOT NULL,
    "Date" VARCHAR(20) NOT NULL,
    "Time" VARCHAR(20) NOT NULL,
    "Payment" VARCHAR(50) NOT NULL,
    "cogs" NUMERIC(12, 2) NOT NULL,
    "gross margin percentage" NUMERIC(10, 6) NOT NULL,
    "gross income" NUMERIC(12, 4) NOT NULL,
    "Rating" NUMERIC(4, 2) NOT NULL
);

--Conferir a estrutura
SELECT *
FROM raw_vendas
LIMIT 5;

--Conferir as colunas
SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_name = 'raw_vendas'
ORDER BY ordinal_position;

--Conferir PRIMARY KEY
SELECT
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
WHERE tc.table_name = 'raw_vendas';
