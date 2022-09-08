import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

st.title("Palmer's Penguins")

st.markdown('Use this Streamlit app to make your own \
            scatterplot about penguins!')

selected_species = st.selectbox(
    label='What species would you like to visualize?', 
    options= ['Adelie', 'Gentoo', 'Chinstrap'],
    )

selected_x_var = st.selectbox(
    label= 'What do want the x variable to be?',
    options= ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    )

selected_y_var = st.selectbox(
    label= 'What about the y?',
    options= ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

#Import Data
penguins_df = pd.read_csv('penguins.csv')

#Filter DF as per selected specie
specie_df = penguins_df[penguins_df['species'] == selected_species]

#Plot
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data= penguins_df,
    x= penguins_df[selected_x_var],
    y= penguins_df[selected_y_var],
    
)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Scatterplot of {} Penguins'.format(selected_species))
st.pyplot(fig)
