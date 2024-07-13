# Learning from Data Professor on Datarockies's Youtube 

import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit world! This is my first app. 🐼")

placeholder = st.empty() # use to update code status such as we want to show our ML status
# status = 1 # success
# status = 0 # fail
status = st.radio(
        "Select an option", 
        ["Success", "Error"])

# if status == 1:
if status == "Success":   
    placeholder.success("Success!")
else:
    # placeholder.error("Error!")
    placeholder.error("Noooo!")

# st.write('Awesome!')
# st.info('Hello again!')
# st.success("This is super cool!")
# st.error("This is an error message.")
# st.warning("This is a worning message.")

st.header('Area chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns = ['a', 'b', 'c']) # create a DataFrame RowxCol
st.area_chart(chart_data) # under the hood of Vega-Altair library - Declarative Visualization in Python
