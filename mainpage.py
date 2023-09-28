import streamlit as st
import pandas as pd
import matplotlib as mp
from streamlit import session_state as ss

st.header("Immersion Tracker")
st.subheader('tracking immersion')



def get_data():

    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame({"X":[1,2,3,4], "Y": [10,20,30,40]})
    return st.session_state.data

data = get_data()

edited_data= st.table(data)

new_value = st.number_input("Enter Number of Mins", key="new_value")
edit_index = st.number_input("Enter an index to edit:", min_value=0, max_value=len(data)-1, key="edit_index")

if st.button("Edit Value"):
    data.at[edit_index, 'Y'] = new_value
    st.session_state.data = data
    st.experimental_rerun
st.line_chart(data)
