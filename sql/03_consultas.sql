-- ============================================================
-- Projeto: Análise de Dados com Python
-- Consultas SQL - Camada Raw
-- ============================================================


-- ============================================================
-- 1. Visualização inicial
-- ============================================================

SELECT *
FROM raw_vendas
LIMIT 10;


-- ============================================================
-- 2. Quantidade de vendas por filial
-- ============================================================

SELECT
    "Branch",
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;


-- ============================================================
-- 3. Receita por filial
-- ============================================================

SELECT
    "Branch",
    SUM("Sales") AS receita_total
FROM raw_vendas
GROUP BY "Branch"
ORDER BY receita_total DESC;


-- ============================================================
-- 4. Receita por linha de produto
-- ============================================================

SELECT
    "Product line",
    SUM("Sales") AS receita_total
FROM raw_vendas
GROUP BY "Product line"
ORDER BY receita_total DESC;


-- ============================================================
-- 5. Avaliação média por linha de produto
-- ============================================================

SELECT
    "Product line",
    AVG("Rating") AS avaliacao_media
FROM raw_vendas
GROUP BY "Product line"
ORDER BY avaliacao_media DESC;


-- ============================================================
-- 6. Forma de pagamento mais utilizada
-- ============================================================

SELECT
    "Payment",
    COUNT(*) AS quantidade
FROM raw_vendas
GROUP BY "Payment"
ORDER BY quantidade DESC;


-- ============================================================
-- 7. Valor médio das vendas
-- ============================================================

SELECT
    AVG("Sales") AS valor_medio_venda
FROM raw_vendas;


-- ============================================================
-- 8. Maior venda
-- ============================================================

SELECT
    "Invoice ID",
    "Branch",
    "Product line",
    "Sales"
FROM raw_vendas
ORDER BY "Sales" DESC
LIMIT 1;


-- ============================================================
-- 9. Vendas por dia da semana
-- ============================================================

SELECT
    EXTRACT(
        DOW FROM TO_DATE("Date", 'MM/DD/YYYY')
    ) AS numero_dia_semana,
    TRIM(
        TO_CHAR(
            TO_DATE("Date", 'MM/DD/YYYY'),
            'Day'
        )
    ) AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY
    numero_dia_semana,
    dia_semana
ORDER BY quantidade_vendas DESC;