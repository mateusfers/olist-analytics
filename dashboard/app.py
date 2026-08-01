import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Olist Dashboard", layout="wide")

st.title("Olist Analytics Dashboard")
st.markdown("---")

@st.cache_data
def load_data():
    df_orders = pd.read_csv('data/raw/olist_orders_dataset.csv')
    df_order_items = pd.read_csv('data/raw/olist_order_items_dataset.csv')
    
    df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
    df_orders['order_delivered_customer_date'] = pd.to_datetime(df_orders['order_delivered_customer_date'])
    df_orders['delivery_time'] = (df_orders['order_delivered_customer_date'] - df_orders['order_purchase_timestamp']).dt.days
    
    df_order_items['total_value'] = df_order_items['price'] + df_order_items['freight_value']
    df_order_total = df_order_items.groupby('order_id')['total_value'].sum().reset_index()
    df_order_total.columns = ['order_id', 'order_total_value']
    
    return df_orders, df_order_total

df_orders, df_order_total = load_data()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Pedidos", f"{len(df_orders):,}")

with col2:
    receita = df_order_total['order_total_value'].sum()
    st.metric("Receita Total", f"R$ {receita:,.2f}")

with col3:
    ticket = df_order_total['order_total_value'].mean()
    st.metric("Ticket Médio", f"R$ {ticket:,.2f}")

with col4:
    tempo = df_orders['delivery_time'].mean()
    st.metric("Tempo Médio de Entrega", f"{tempo:.1f} dias")

st.markdown("---")

st.subheader("Últimos Pedidos")
st.dataframe(df_orders[['order_id', 'order_purchase_timestamp', 'order_status']].head(10))

st.markdown("---")

st.subheader("Distribuição do Tempo de Entrega")

fig, ax = plt.subplots(figsize=(10, 4))
sns.histplot(df_orders['delivery_time'].dropna(), bins=30, kde=True)
plt.xlabel('Dias')
plt.ylabel('Frequência')
st.pyplot(fig)