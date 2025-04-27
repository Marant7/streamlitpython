import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título del Dashboard
st.title("Dashboard de Ventas de Tienda en Línea")

# Simulamos algunos datos de ventas
np.random.seed(0)
fechas = pd.date_range(start='2023-01-01', periods=100, freq='D')
ventas = np.random.randint(10, 100, size=100)
productos = np.random.choice(['Producto A', 'Producto B', 'Producto C'], size=100)

# Crear DataFrame
df = pd.DataFrame({'Fecha': fechas, 'Ventas': ventas, 'Producto': productos})

# Mostrar las primeras filas de los datos
st.write("Datos de Ventas:", df.head())

# Filtro de fechas
fecha_inicio = st.date_input('Fecha de inicio', df['Fecha'].min())
fecha_fin = st.date_input('Fecha de fin', df['Fecha'].max())

# Filtrar los datos según el rango de fechas
df_filtrado = df[(df['Fecha'] >= pd.to_datetime(fecha_inicio)) & (df['Fecha'] <= pd.to_datetime(fecha_fin))]

# Mostrar el resumen de los datos filtrados
st.write(f"Datos filtrados entre {fecha_inicio} y {fecha_fin}", df_filtrado)

# Generar Gráficos

# Gráfico de Ventas por Fecha
fig, ax = plt.subplots()
ax.plot(df_filtrado['Fecha'], df_filtrado['Ventas'], label='Ventas Diarias', color='blue')
ax.set_title('Ventas Diarias')
ax.set_xlabel('Fecha')
ax.set_ylabel('Ventas')
st.pyplot(fig)

# Gráfico de Ventas por Producto
ventas_por_producto = df_filtrado.groupby('Producto')['Ventas'].sum()
fig2, ax2 = plt.subplots()
ax2.bar(ventas_por_producto.index, ventas_por_producto.values, color='green')
ax2.set_title('Ventas por Producto')
ax2.set_xlabel('Producto')
ax2.set_ylabel('Ventas')
st.pyplot(fig2)

# Generar un Reporte de Ventas
st.subheader("Reporte de Ventas")

# Mostrar resumen de ventas
ventas_totales = df_filtrado['Ventas'].sum()
ventas_promedio = df_filtrado['Ventas'].mean()
producto_mas_vendido = ventas_por_producto.idxmax()

# Mostrar el reporte
st.write(f"Total de ventas: {ventas_totales}")
st.write(f"Promedio de ventas: {ventas_promedio:.2f}")
st.write(f"Producto más vendido: {producto_mas_vendido}")

# Botón para descargar el reporte como texto
if st.button("Generar Reporte en Texto"):
    reporte = f"""
    Reporte de Ventas:
    
    Total de ventas: {ventas_totales}
    Promedio de ventas: {ventas_promedio:.2f}
    Producto más vendido: {producto_mas_vendido}
    """
    st.text(reporte)