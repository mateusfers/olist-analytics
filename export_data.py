import pandas as pd

print("📊 Exportando dados para Power BI...")

# Carregar dados
df_orders = pd.read_csv('data/raw/olist_orders_dataset.csv')
df_order_items = pd.read_csv('data/raw/olist_order_items_dataset.csv')
df_products = pd.read_csv('data/raw/olist_products_dataset.csv')
df_customers = pd.read_csv('data/raw/olist_customers_dataset.csv')
df_order_reviews = pd.read_csv('data/raw/olist_order_reviews_dataset.csv')

# Converter datas
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
df_orders['order_delivered_customer_date'] = pd.to_datetime(df_orders['order_delivered_customer_date'])

# Calcular delivery_time
df_orders['delivery_time'] = (df_orders['order_delivered_customer_date'] - df_orders['order_purchase_timestamp']).dt.days

# Calcular valor total do pedido
df_order_items['total_value'] = df_order_items['price'] + df_order_items['freight_value']
df_order_total = df_order_items.groupby('order_id')['total_value'].sum().reset_index()
df_order_total.columns = ['order_id', 'order_total_value']

# Extrair features de data
df_orders['purchase_month'] = df_orders['order_purchase_timestamp'].dt.month
df_orders['purchase_year'] = df_orders['order_purchase_timestamp'].dt.year
df_orders['purchase_day_name'] = df_orders['order_purchase_timestamp'].dt.day_name()

# Juntar todas as tabelas
df_final = df_orders.merge(df_customers, on='customer_id', how='left')
df_final = df_final.merge(df_order_total, on='order_id', how='left')
df_final = df_final.merge(df_order_reviews, on='order_id', how='left')

# Salvar
df_final.to_csv('data/processed_data.csv', index=False)
print(f"✅ {len(df_final)} registros salvos em data/processed_data.csv")
print("✅ Dados prontos para o Power BI!")