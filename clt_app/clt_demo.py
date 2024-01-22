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


