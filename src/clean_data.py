import pandas as pd

def clean_orders(df):
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    return df

def add_delivery_time(df):
    df['delivery_time'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    return df

def add_date_features(df):
    df['purchase_month'] = df['order_purchase_timestamp'].dt.month
    df['purchase_year'] = df['order_purchase_timestamp'].dt.year
    df['purchase_day_of_week'] = df['order_purchase_timestamp'].dt.dayofweek
    df['purchase_day_name'] = df['order_purchase_timestamp'].dt.day_name()
    df['is_weekend'] = df['purchase_day_name'].isin(['Saturday', 'Sunday'])
    return df