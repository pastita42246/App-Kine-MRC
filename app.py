import streamlit as st
from modulo_ena import mostrar_ena  # <--- Esta es la línea clave que conecta los archivos

def main():
    st.set_page_config(page_title="App Clínica - Kine", layout="centered")
    
    st.title("Sistema de Evaluación Clínica ⚡")
    st.write("Bienvenido, selecciona el test que deseas realizar:")

    # Aquí llamamos a la función que vive en tu otro archivo
    nivel_dolor = mostrar_ena()

    # Si quisieras agregar más tests luego, solo añadirás líneas aquí abajo
    # st.write("---")
    # st.write("Próximo test: MRC Sum Score...")

if __name__ == "__main__":
    main()
