import streamlit as st
import pandas as pd
import matplotlib as mp
from streamlit import session_state as ss

st.header("Books")

if 'times2' not in ss:
    ss['times2'] = None


def get_data2():

    if "data2" not in st.session_state:
        st.session_state.data2 = pd.DataFrame({"Which day":[1,2,3,4,5,6,7], "How many minutes": [0,0,0,0,0,0,0]})
    return st.session_state.data2
    
data2 = get_data2()
ss.times2 = data2['How many minutes'].tolist()
edited_data= st.table(data2)

new_value = st.number_input("Enter Number of Mins", key="new_value")
edit_index = st.number_input("Enter an index to edit:", min_value=0, max_value=len(data2)-1, key="edit_index")

if st.button("Edit Value"):
    data2.at[edit_index, 'How many minutes'] = new_value
    st.session_state.data = data2
    st.experimental_rerun
st.line_chart(data2)