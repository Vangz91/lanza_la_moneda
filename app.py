import streamlit as st
import random

# Título de la aplicación
st.header('Lanzar una moneda')

# Instrucción de la aplicación
st.write('Haz clic en el botón para lanzar una moneda.')

# Botón para lanzar la moneda
if st.button('Lanzar moneda'):
    resultado = random.choice(['Cara', 'Cruz'])
    st.write(f'El resultado es: {resultado}')
