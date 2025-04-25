import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Visualización Interactiva de Datos con Streamlit")

# Generar datos aleatorios
n = st.slider("Número de puntos", min_value=100, max_value=10000, value=500)
data = np.random.randn(n)

# Mostrar gráfico interactivo
fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor='black')
ax.set_title("Distribución de Datos Aleatorios")
ax.set_xlabel("Valor")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

# Explicación del gráfico
st.write("""
Este gráfico muestra una distribución de datos generados aleatoriamente.
Puedes interactuar con el control deslizante para ajustar el número de puntos en la distribución.
""")