import streamlit as st

def mostrar_ena():
    st.subheader("Escala Numérica Análoga (ENA) - Dolor")
    
    dolor = st.select_slider(
        "¿Cómo califica su nivel de dolor actual?",
        options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        value=0
    )

    if dolor == 0:
        st.success(f"Nivel {dolor}: Sin dolor")
    elif 1 <= dolor <= 3:
        st.warning(f"Nivel {dolor}: Dolor Leve")
    elif 4 <= dolor <= 6:
        st.warning(f"Nivel {dolor}: Dolor Moderado")
    else:
        st.error(f"Nivel {dolor}: Dolor Severo")
        
    return dolor
