import streamlit as st
from drawer import DataDrawer

#Initial settings
st.set_page_config(page_title="کافی من", page_icon="☕️")

dd = DataDrawer('data/CafeSales.csv')
st.plotly_chart(dd.plot_stores())