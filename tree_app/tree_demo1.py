import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


st.title("San Francisco Trees")

st.write('This app analyses trees in San Francisco using'
' a dataset kindly provided by SF DPW')

trees_df = pd.read_csv('trees.csv')

groupby_dbh_df = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])

st.subheader('Trees Grouped By Tree Width')

st.write(groupby_dbh_df.head())

groupby_dbh_df.columns = ['tree_count']

#Draw a Line Chart Using Streamlit in-built line charts
st.line_chart(groupby_dbh_df)

#Draw an Area Chart Using Streamlit in-built area charts
st.area_chart(groupby_dbh_df)

#Draw a Bar Chart Using Streamlit in-built bar charts
st.bar_chart(groupby_dbh_df)

#Adding a new column to the new df
groupby_dbh_df['new_col'] = np.random.randn(len(groupby_dbh_df)) * 500
st.line_chart(groupby_dbh_df)


""" 
#st.map()

Finds columns that it thinks are longitude and latitude points 
by searching the DataFrame for columns with titles such as longitude,
long, latitude, or lat. Then, it plots each row as its own point on a map, 
auto-zooms and focuses the map, and writes it to our Streamlit app

"""
map_of_trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
map_of_trees_df = map_of_trees_df.sample(n = 1000)

st.map(map_of_trees_df)

#Plotting Plotly Graphs
st.subheader('Plotly Chart')

fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

#Plotting Seaborn Charts
st.subheader('Seaborn Chart')

trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days

fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_sb)

#Plotting Matplotlib Charts
st.subheader('Matploblib Chart')

fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_mpl)
