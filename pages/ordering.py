import streamlit as st
import polars as pl
import numpy as np
import datetime
import json

# Load products from JSON file
with open('pages/pages_utils/products.json') as file:
    products = json.load(file)

# Initialize session state for orders if it doesn't exist
if "orders" not in st.session_state:
    st.session_state.orders = pl.DataFrame()

# Sidebar for user input
with st.sidebar:
    customer_id = st.text_input(label='آیدی مشتری')
    product = st.selectbox('محصولات', list(products.keys()))
    quantity = st.number_input('تعداد', step=1)

    if st.button('افزودن'):
        # Create a new order DataFrame
        new_order = pl.DataFrame({
            'تاریخ': [datetime.datetime.today().strftime('%Y-%m-%d')],
            'ساعت': [datetime.datetime.today().hour],
            'محصول': [product],
            'آیدی فروشگاه': [0],
            'تعداد': [quantity],
            'قیمت واحد': [products[product]],
            'آیدی مشتری': [customer_id]
        })

        # Update session state orders DataFrame
        st.session_state.orders = pl.concat([st.session_state.orders, new_order])

# Display the orders if there are any
if not st.session_state.orders.is_empty():
    st.dataframe(st.session_state.orders, width=200, use_container_width=True)
else:
    st.write("No orders yet.")
