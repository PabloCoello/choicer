import streamlit as st
import pandas as pd

# Configuración del título de la página
st.title("Choicer!!")

# Creación de un sidebar
st.sidebar.header("Opciones")

# Añadir elementos al sidebar
opcion_1 = st.sidebar.checkbox("Mostrar información adicional")

# Texto en la página principal
st.write("""
Esta es una aplicación básica de Streamlit. Puedes personalizarla según tus necesidades.
""")

prompt = st.text_area("Ingrese su texto aquí", "Escribe aquí...", height=100)

# Verificar la opción del sidebar y mostrar información adicional si está seleccionada
if opcion_1:
    st.write("¡Información adicional visible!")

# Crear un DataFrame de ejemplo para la tabla de markdown
data = {'Nombre': ['Juan', 'María', 'Carlos'],
        'Edad': [25, 30, 22],
        'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad C']}
df = pd.DataFrame(data)

# Mostrar tabla de markdown
st.write("### Tabla de Datos:")
st.markdown(df.to_markdown(), unsafe_allow_html=True)