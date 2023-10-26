import streamlit as st
import pandas as pd
import matplotlib as mp
from streamlit import session_state as ss

st.header("Shows")

if 'times3' not in ss:
    ss['times3'] = None


def get_data3():

    if "data3" not in st.session_state:
        st.session_state.data3 = pd.DataFrame({"Which day":[1,2,3,4,5,6,7], "How many minutes": [0,0,0,0,0,0,0]})
    return st.session_state.data3

data3 = get_data3()
ss.times3 = data3['How many minutes'].tolist()
edited_data= st.table(data3)

new_value = st.number_input("Enter Number of Mins", key="new_value")
edit_index = st.number_input("Enter an index to edit:", min_value=0, max_value=len(data3)-1, key="edit_index")

if st.button("Edit Value"):
    data3.at[edit_index, 'How many minutes'] = new_value
    st.session_state.data = data3
    st.experimental_rerun
st.line_chart(data3)