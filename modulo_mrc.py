import streamlit as st

def mostrar_mrc():
    st.markdown("---")
    st.subheader("MRC Sum Score (60 puntos) 💪")
    st.write("Evalúa los 6 grupos musculares en ambos hemicuerpos (0 = Nulo, 5 = Normal).")

    # Dividimos la pantalla en 2 columnas
    col_derecha, col_izquierda = st.columns(2)

    with col_derecha:
        st.markdown("**Hemicuerpo Derecho**")
        hombro_d = st.slider("Abducción Hombro (Der)", 0, 5, 5)
        codo_d = st.slider("Flexión Codo (Der)", 0, 5, 5)
        muneca_d = st.slider("Extensión Muñeca (Der)", 0, 5, 5)
        cadera_d = st.slider("Flexión Cadera (Der)", 0, 5, 5)
        rodilla_d = st.slider("Extensión Rodilla (Der)", 0, 5, 5)
        tobillo_d = st.slider("Dorsiflexión Tobillo (Der)", 0, 5, 5)

    with col_izquierda:
        st.markdown("**Hemicuerpo Izquierdo**")
        hombro_i = st.slider("Abducción Hombro (Izq)", 0, 5, 5)
        codo_i = st.slider("Flexión Codo (Izq)", 0, 5, 5)
        muneca_i = st.slider("Extensión Muñeca (Izq)", 0, 5, 5)
        cadera_i = st.slider("Flexión Cadera (Izq)", 0, 5, 5)
        rodilla_i = st.slider("Extensión Rodilla (Izq)", 0, 5, 5)
        tobillo_i = st.slider("Dorsiflexión Tobillo (Izq)", 0, 5, 5)

    # Procesamiento: Suma matemática total
    puntaje_total = (
        hombro_d + codo_d + muneca_d + cadera_d + rodilla_d + tobillo_d +
        hombro_i + codo_i + muneca_i + cadera_i + rodilla_i + tobillo_i
    )

    # Salida Visual del Diagnóstico
    st.write("---")
    st.subheader(f"Puntaje Total: {puntaje_total} / 60")

    if puntaje_total == 60:
        st.success("Diagnóstico: Fuerza muscular global conservada.")
    elif puntaje_total >= 48:
        st.warning("Diagnóstico: Debilidad muscular leve a moderada. Monitorear progresión.")
    else:
        st.error("Diagnóstico: Debilidad neuromuscular significativa (Cuadriparesia / Polineuropatía clínica posible).")

    return puntaje_total
