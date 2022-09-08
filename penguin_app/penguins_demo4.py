import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

st.title("Palmer's Penguins")

st.markdown('Use this Streamlit app to make your own \
            scatterplot about penguins!')


selected_x_var = st.selectbox(
    label= 'What do want the x variable to be?',
    options= ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    )

selected_y_var = st.selectbox(
    label= 'What about the y?',
    options= ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

#Upload Data
penguins_file = st.file_uploader(
    label="Select Your Local Penguins CSV (default provided)"
)

#Filter by gender
selected_gender = st.selectbox(
    label='What gender do you want to filter for?',
    options= ['All Penguins', 'Male Penguins', 'Female Penguins']
    )

if penguins_file is not None:
    penguins_df = pd.read_csv(penguins_file)
else:
    #Using Default
    #penguins_df = pd.read_csv('penguins.csv')

    #Using Stop() to stop the all app till file is uploaded
    st.stop()

if selected_gender == 'Male Penguins':
    penguins_df = penguins_df.loc[penguins_df['sex'] == 'male']
elif selected_gender == 'Female Penguins':
    penguins_df = penguins_df.loc[penguins_df['sex'] == 'female']
else:
    pass



#Plot
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data= penguins_df,
    x= penguins_df[selected_x_var],
    y= penguins_df[selected_y_var],
    hue= penguins_df['species'],
    markers= markers,
    style= 'species',
)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins: {}". format(selected_gender))
st.pyplot(fig)
