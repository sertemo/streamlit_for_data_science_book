"""Script para "probar el teorema de  estadística de centro límite
"""

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Central Limit Theorem")

binom_dist = np.random.binomial(1, .5, 1000)
list_of_means = []
for i in range(0, 1000):
    pick_random = np.random.choice(binom_dist, 100, replace=True)
    list_of_means.append(np.mean(pick_random))

# fig, ax = plt.subplots()
# ax = plt.hist(list_of_means)
# st.pyplot(fig)
# Otra opción:
# plt.hist(list_of_means)
# st.pyplot(plt)
# plt.hist([1, 1, 1, 1])
# st.pyplot(plt)
# No es aconsejable NO asignar la salida del grafico a una variable
# Lo mejor es hacerlo asi:
fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means)
st.pyplot(fig1)
fig2, ax2 = plt.subplots()
ax2 = plt.hist([1, 1, 1, 1])
st.pyplot(fig2)

st.title('Illustrating the Central Limit Theorem with Streamlit') 
st.header('An App by STM 2024 (c)') 
st.write(('''This app simulates a thousand coin flips using the chance of heads input below,  
and then samples with replacement from that population and plots the histogram of the
means of the samples, in order to illustrate the Central Limit Theorem!''')) 


perc_heads = st.number_input(label='Chance of Coins Landing on Heads', min_value=0.0, max_value=1.0, value=.5) 
graph_title = st.text_input('Graph Title')

binom_dist = np.random.binomial(1, perc_heads, 1000) 

list_of_means = []
for i in range(0, 1000): 
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean()) 

fig, ax = plt.subplots() 
ax = plt.hist(list_of_means, range=[0, 1]) 
plt.title(graph_title)

st.pyplot(fig)

st.markdown("""
            # Hola
            ## Hola
            ### Hola""")

