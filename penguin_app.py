# Learning from Data Professor on Datarockies's Youtube 

import pandas as pd
import streamlit as st
import altair as alt

# import penguin cleaned csv to a DataFrame
penguin_df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
penguin_df

# https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart
c = (
   alt.Chart(penguin_df)
   .mark_circle()
   .encode(x = "bill_length_mm", 
           y = "body_mass_g", 
           color = "species")
).interactive()

st.altair_chart(c, use_container_width = True)