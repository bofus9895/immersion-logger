
import streamlit as st
import pandas as pd
from streamlit import session_state as ss
st.title('Immersion Logger')
st.markdown('click on all pages to get rid of error')
bigdata=st.dataframe({"Which day":[1,2,3,4,5,6,7], "How many minutes on shows": ss.times3, "How many minutes on books": ss.times2, "How many minutes on vns": ss.times1})
bigdata=pd.DataFrame({"Which day":[1,2,3,4,5,6,7], "How many minutes on shows": ss.times3, "How many minutes on books": ss.times2, "How many minutes on vns": ss.times1})
st.line_chart(bigdata)
tdataadd3 = bigdata['How many minutes on shows'].tolist()
tdataadd2 = bigdata['How many minutes on books'].tolist()
tdataadd1 = bigdata['How many minutes on vns'].tolist()
#doendt wokr
#weektime = [0,0,0,0,0,0,0]
#for x in weektime:
#    weektime.index(x) + tdataadd3.index(x) + tdataadd1.index(x) + tdataadd2.index(x)

#st.line_chart(weektime)
