import streamlit as st
import pandas as pd
import matplotlib as mp
import numpy as np


st.header("Incel Tracker")
st.subheader('tracking things for incels')

chart_data = pd.DataFrame({
    'ami1' : np.random.randn(20),
    'ami2' : np.random.randn(20),
    'ami3' : np.random.choice(['A','B','C'],20)
})

st.bar_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col3'
)

chart_data = pd.DataFrame({
    'mg1' : np.random.randn(20),
    'mg2' : np.random.randn(20),
    'ami3' : np.random.choice(['A','B','C'],20)
})

st.bar_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col3'
)

chart_data = pd.DataFrame({
    'vm1' : np.random.randn(20),
    'vm2' : np.random.randn(20),
    'vm3' : np.random.choice(['A','B','C'],20)
})

st.bar_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col3'
)

