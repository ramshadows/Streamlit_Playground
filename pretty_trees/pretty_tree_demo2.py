#Working With Streamlit SideBar

import streamlit as st
import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')


trees_df = pd.read_csv('trees.csv')

trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days

owners = st.sidebar.multiselect(
    label='Select Tree Caretaker',
    options=trees_df['caretaker'].unique()
)



st.title("San Francisco Trees")

st.write('This app analyses trees in San Francisco using'
' a dataset kindly provided by SF DPW')

st.write('The current analysis is of trees owned by {}'.
format(owners))

if owners:
   tree_df = trees_df[trees_df['caretaker'].isin(owners)]


#define multiple columns, add two graphs
col1, col2 = st.columns(2)

with col1:
    st.write('Trees by Width')
    fig_1, ax_1 = plt.subplots()
    ax_1 = sns.histplot(trees_df['dbh'])
    plt.xlabel('Tree Width')
    st.pyplot(fig_1)

with col2:
    st.write('Trees by Age')
    fig_2, ax_2 = plt.subplots()
    ax_2 = sns.histplot(trees_df['age'])
    plt.xlabel('Age (Days)')
    st.pyplot(fig_2)

st.write('Trees by Location')
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000, replace=True)
st.map(trees_df)









