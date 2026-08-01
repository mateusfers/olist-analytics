import pandas as pd

def add_order_total(df_order_items):
    df_order_items['total_item_value'] = df_order_items['price'] + df_order_items['freight_value']
    df_order_total = df_order_items.groupby('order_id')['total_item_value'].sum().reset_index()
    df_order_total.columns = ['order_id', 'order_total_value']
    return df_order_total