#Working With Streamlit Columns

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title("San Francisco Trees")

st.write('This app analyses trees in San Francisco using'
' a dataset kindly provided by SF DPW')

trees_df = pd.read_csv('trees.csv')

groupby_dbh_df = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])

st.subheader('Trees Grouped By Tree Width')

groupby_dbh_df.columns = ['tree_count']

col1, col2, col3 = st.columns((10, 10, 10))

with col1:
    st.write('First Column')

    #Draw a Line Chart Using Streamlit in-built line charts
    st.line_chart(groupby_dbh_df)

with col2:
    st.write('Second Column')

    #Draw an Area Chart Using Streamlit in-built area charts
    st.area_chart(groupby_dbh_df)

with col3:
    st.write('Thrd Column')

    #Draw a Bar Chart Using Streamlit in-built bar charts
    st.bar_chart(groupby_dbh_df)