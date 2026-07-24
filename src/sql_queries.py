import sqlite3
import pandas as pd

def criar_banco_dados(df_orders, df_order_items, df_products, df_sellers, df_customers):
    # Conectar ao bd
    conn = sqlite3.connect('data/olist.db')
    
    # Salvar cada DataFrame como tabela
    df_orders.to_sql('orders', conn, if_exists='replace', index=False)
    df_order_items.to_sql('order_items', conn, if_exists='replace', index=False)
    df_products.to_sql('products', conn, if_exists='replace', index=False)
    df_sellers.to_sql('sellers', conn, if_exists='replace', index=False)
    df_customers.to_sql('customers', conn, if_exists='replace', index=False)
    
    print("Tabelas sucesso!")
    
    # Fechar
    conn.close()
    return conn

def executar_query(query):
    conn = sqlite3.connect('data/olist.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def query_estado_mais_pedidos():
    query = """
        SELECT
            c.customer_state AS estado,
            COUNT(o.order_id) AS total_pedidos
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.customer_state
        ORDER BY total_pedidos DESC
        LIMIT 10
    """
    df = executar_query(query)
    print(df)
    return df

def query_categoria_maior_faturamento():
    query = """
        SELECT
            p.product_category_name AS categoria,
            ROUND(SUM(oi.price), 2) AS faturamento_total
        FROM order_items oi
        INNER JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.product_category_name
        ORDER BY faturamento_total DESC
        LIMIT 10
    """
    df = executar_query(query)
    print(df)
    return df


if __name__ == "__main__":
    print("Carregando dados...")
    
    df_orders = pd.read_csv('data/raw/olist_orders_dataset.csv')
    df_order_items = pd.read_csv('data/raw/olist_order_items_dataset.csv')
    df_products = pd.read_csv('data/raw/olist_products_dataset.csv')
    df_sellers = pd.read_csv('data/raw/olist_sellers_dataset.csv')
    df_customers = pd.read_csv('data/raw/olist_customers_dataset.csv')
    
    criar_banco_dados(df_orders, df_order_items, df_products, df_sellers, df_customers)
    query_estado_mais_pedidos()
    query_categoria_maior_faturamento()
