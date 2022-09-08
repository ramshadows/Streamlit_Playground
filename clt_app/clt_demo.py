import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Illustrating the Central Limit Theorem Using Streamlit')
st.subheader('An App by Rafael')

st.write(('This app simulates a thousand coin flips using the \
chance of heads input below,' \
'and then samples with replacement from that population \
and plots the histogram of the' \
' means of the samples, in order to illustrate the Central \
Limit Theorem!'))

percentage_chance = st.number_input(
    label='Chance of Coin Landing on Heads', min_value=0.0,
    max_value=1.0,
    value= .5,
)

#graph_title = st.text_input(label='Histogram of Mean of Binomial Distribution')

binomial_dist = np.random.binomial(1, percentage_chance, 1000)

list_of_means = []

for i in range(1, 1000):
    list_of_means.append(np.random.choice(binomial_dist, 100, replace=True)
    .mean())

fig, ax = plt.subplots()
ax = plt.hist(list_of_means, range=[0, 1],)
plt.title('Histogram of Mean of Binomial Distribution')
st.pyplot(fig)