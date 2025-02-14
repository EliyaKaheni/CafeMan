import streamlit as st
import polars as pl
import numpy as np
import datetime
import json


# Load products from JSON file
with open('pages/pages_utils/products.json') as file:
    products = json.load(file)

# Initial settings
st.set_page_config(layout="wide")
if "orders" not in st.session_state:
    st.session_state.orders = pl.DataFrame()

with st.sidebar:
    customer_id = st.text_input(label='آیدی مشتری')
    product = st.selectbox('محصولات', list(products.keys()))
    quantity = st.number_input('تعداد', step=1)

    # Adding new order
    if st.button('افزودن'):
        new_order = pl.DataFrame({
            'تاریخ': [datetime.datetime.today().strftime('%Y-%m-%d')],
            'ساعت': [datetime.datetime.today().hour],
            'محصول': [product],
            'آیدی فروشگاه': [0],
            'تعداد': [quantity],
            'قیمت واحد': [products[product]],
            'آیدی مشتری': [customer_id]
        })

        st.session_state.orders = pl.concat([st.session_state.orders, new_order])
    
    # Deleting the last row
    if st.button('حذف آخرین ردیف'):
        if not st.session_state.orders.is_empty():
            st.session_state.orders = st.session_state.orders.slice(0, -1)

# Displaying the orders
if not st.session_state.orders.is_empty():
    total_quantity = st.session_state.orders['تعداد'].sum()
    total_price = (st.session_state.orders['تعداد'] * st.session_state.orders['قیمت واحد']).sum()

    summation_row = pl.DataFrame({
        'تاریخ': [datetime.datetime.today().strftime('%Y-%m-%d')],
        'ساعت': [datetime.datetime.today().hour],
        'محصول': ['جمع کل سفارش'],
        'آیدی فروشگاه': [0],
        'تعداد': [total_quantity],
        'قیمت واحد': [total_price],
        'آیدی مشتری': [customer_id]
    })

    orders_with_sum = pl.concat([summation_row, st.session_state.orders])

    st.dataframe(orders_with_sum, width=1000, use_container_width=True)

else:
    st.write("سفارشی ثبت نشده است.")