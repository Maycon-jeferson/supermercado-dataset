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

--======================================================
--Apos os dados serem carregados no banco, podemos conferir a quantidade de registros
========================================================

--Contagem de registros
SELECT COUNT(*)
FROM raw_vendas;

SELECT COUNT(*) AS total_registros
FROM raw_vendas;

--Verificacao de dados
SELECT *
FROM raw_vendas
LIMIT 5;

--Verificar o ID
SELECT
    COUNT(*) AS total,
    COUNT(DISTINCT "Invoice ID") AS ids_unicos
FROM raw_vendas;

--Verifica se exite registro nulos no banco
SELECT
    COUNT(*) FILTER (WHERE "Invoice ID" IS NULL) AS invoice_id_nulos,
    COUNT(*) FILTER (WHERE "Branch" IS NULL) AS branch_nulos,
    COUNT(*) FILTER (WHERE "City" IS NULL) AS city_nulos,
    COUNT(*) FILTER (WHERE "Sales" IS NULL) AS sales_nulos,
    COUNT(*) FILTER (WHERE "Rating" IS NULL) AS rating_nulos
FROM raw_vendas;

--Validação de valores
SELECT
    MIN("Sales") AS menor_venda,
    MAX("Sales") AS maior_venda,
    AVG("Sales") AS media_venda
FROM raw_vendas;

SELECT
    MIN("Quantity") AS menor_quantidade,
    MAX("Quantity") AS maior_quantidade,
    AVG("Quantity") AS media_quantidade
FROM raw_vendas;

--Validação de datas
SELECT 
    MIN("Date") AS data_inicial,
    MAX("Date") AS data_final
FROM raw_vendas;

--Validação de horários
SELECT
    MIN("Time") AS horario_inicial,
    MAX("Time") AS horario_final
FROM raw_vendas;

--Validação de ratings
SELECT
    MIN("Rating") AS menor_rating,
    MAX("Rating") AS maior_rating,
    AVG("Rating") AS media_rating
FROM raw_vendas;


