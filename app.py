import streamlit as st
from modulo_ena import mostrar_ena
from modulo_mrc import mostrar_mrc  # 1. Traemos la herramienta en la mochila

def main():
    st.set_page_config(page_title="App Clínica - Kine", layout="centered")
    
    st.title("Sistema de Evaluación Clínica ⚡")
    st.write("Bienvenido, completa la evaluación del paciente:")

    # 2. Ejecutamos el primer test (Dolor)
    nivel_dolor = mostrar_ena()

    # 3. Ejecutamos el segundo test (MRC Sum Score)
    puntaje_mrc = mostrar_mrc()

if __name__ == "__main__":
    main()
