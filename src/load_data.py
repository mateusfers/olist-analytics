import pandas as pd

def load_orders():
    return pd.read_csv('C:/Users/Mateus Fernandes/Documents/olist-analytics/data/raw/olist_orders_dataset.csv')

def load_order_items():
    return pd.read_csv('C:/Users/Mateus Fernandes/Documents/olist-analytics/data/raw/olist_order_items_dataset.csv')

def load_products():
    return pd.read_csv('C:/Users/Mateus Fernandes/Documents/olist-analytics/data/raw/olist_products_dataset.csv')

def load_customers():
    return pd.read_csv('C:/Users/Mateus Fernandes/Documents/olist-analytics/data/raw/olist_customers_dataset.csv')

def load_reviews():
    return pd.read_csv('C:/Users/Mateus Fernandes/Documents/olist-analytics/data/raw/olist_order_reviews_dataset.csv')

def load_sellers():
    return pd.read_csv('C:/Users/Mateus Fernandes/Documents/olist-analytics/data/raw/olist_sellers_dataset.csv')