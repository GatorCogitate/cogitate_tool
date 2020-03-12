import streamlit as st
import numpy as np
import pandas as pd

st.title("Commit Information")  # dispaly relevant title for dataframe

df = pd.DataFrame({
  'date': ['10/1/2019','10/2/2019', '10/3/2019', '10/4/2019'],
  'Christian Lussier': [8, 5, 9, 3],
  'Cory Wiard': [5, 9, 3, 5],
  'Devin Spitalny': [2, 5, 7, 3],
  'Devin Ho': [8, 9, 2, 1],
  'Jordan Wilson': [5, 9, 3, 8],
  'Danny Reid': [5, 4, 3, 5],
  'Anthony Baldeosingh': [1, 2, 1, 2],
  'Xingbang Liu': [6, 9, 4, 7]
})  # create dataframe with sample dates and contributor commit numbers

df = df.rename(columns={'date':'index'}).set_index('index')  # set date as index

df  # display chart of sample commits

columns = st.multiselect(
    label="Enter the names of specific contributors below:", options=df.columns
)  # allow users to display specific contributor information on dataframe graph

st.line_chart(df[columns])  # display dataframe/graph that vizualizes commit info
