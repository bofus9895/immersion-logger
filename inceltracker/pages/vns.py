import streamlit as st
import pandas as pd
import matplotlib as mp
from streamlit import session_state as ss

st.header("Visual Novels")

if 'times1' not in ss:
    ss['times1'] = None


def get_data1():

    if "data1" not in st.session_state:
        st.session_state.data1 = pd.DataFrame({"Which day":[1,2,3,4,5,6,7], "How many minutes": [0,0,0,0,0,0,0]})
    return st.session_state.data1

data1 = get_data1()
ss.times1 = data1['How many minutes'].tolist()
edited_data= st.table(data1)

new_value = st.number_input("Enter Number of Mins", key="new_value")
edit_index = st.number_input("Enter an index to edit:", min_value=0, max_value=len(data1)-1, key="edit_index")

if st.button("Edit Value"):
    data1.at[edit_index, 'How many minutes'] = new_value
    st.session_state.data = data1
    st.experimental_rerun
st.line_chart(data1)