-- ========================================
-- ANÁLISE DE DADOS OLIST - CONSULTAS SQL
-- ========================================

-- ========================================
-- PERGUNTA 1: Qual estado tem mais pedidos?
-- ========================================
-- RESULTADO: SP (São Paulo) com 41.746 pedidos
-- INSIGHT: SP concentra ~42% dos pedidos
-- ========================================
SELECT 
    c.customer_state AS estado,
    COUNT(o.order_id) AS total_pedidos
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY total_pedidos DESC
LIMIT 10;

-- ========================================
-- PERGUNTA 2: Qual categoria tem maior faturamento?
-- ========================================
-- RESULTADO: beleza_saude com R$ 1.258.681,35
-- INSIGHT: Categorias de consumo pessoal lideram
-- ========================================
SELECT 
    p.product_category_name AS categoria,
    ROUND(SUM(oi.price), 2) AS faturamento_total
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY faturamento_total DESC
LIMIT 10;