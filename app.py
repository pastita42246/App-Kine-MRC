import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuración de la interfaz
st.set_page_config(page_title="App Clínica - MRC", layout="centered")
st.title("Evaluación Muscular: Escala MRC ⚡")

# 2. Inicializar la "Memoria" (Persistencia de datos temporal)
if "historial_pacientes" not in st.session_state:
    st.session_state.historial_pacientes = []

# 3. Entrada de Datos Clínicos
paciente_id = st.text_input("Identificador del Paciente (Ej: Iniciales o RUT):")
grado_mrc = st.slider("Selecciona el Grado MRC evaluado:", min_value=0, max_value=5, value=3)

# 4. Procesamiento: Lógica de diagnóstico
def evaluar_mrc(grado):
    if grado == 5:
        return "Normal", "Vence gravedad y resiste fuerza máxima. Función completa."
    elif grado == 4:
        return "Bueno", "Vence gravedad y soporta resistencia moderada."
    elif grado == 3:
        return "Regular", "Vence la gravedad, pero falla ante cualquier resistencia externa."
    elif grado == 2:
        return "Deficiente", "Movimiento activo solo en plano a favor de la gravedad."
    elif grado == 1:
        return "Vestigios", "Contracción visible/palpable sin movimiento articular."
    else:
        return "Nulo", "Ausencia total de contracción. Parálisis."

clasificacion, mensaje_clinico = evaluar_mrc(grado_mrc)

# 5. Salida Visual Inmediata
st.subheader(f"Resultado Actual: Grado {grado_mrc} - {clasificacion}")

if grado_mrc >= 4:
    st.success(f"✅ {mensaje_clinico}")
elif grado_mrc == 3:
    st.warning(f"⚠️ {mensaje_clinico}")
else:
    st.error(f"🚨 {mensaje_clinico}")

# 6. Acción de Guardado en la Base de Datos
if st.button("Guardar Evaluación"):
    if paciente_id == "":
        st.error("Error: Debes ingresar el identificador del paciente para guardar.")
    else:
        # Creamos un "diccionario" con la información estructurada
        nuevo_registro = {
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Paciente": paciente_id,
            "Grado": grado_mrc,
            "Clasificación": clasificacion
        }
        # Lo inyectamos en la memoria
        st.session_state.historial_pacientes.append(nuevo_registro)
        st.success("¡Registro guardado exitosamente!")

# 7. Visualización del Historial Clínico
if len(st.session_state.historial_pacientes) > 0:
    st.write("---")
    st.subheader("📊 Historial de Evaluaciones")
    # Convertimos la memoria en una tabla profesional usando Pandas
    df_historial = pd.DataFrame(st.session_state.historial_pacientes)
    st.dataframe(df_historial, use_container_width=True)
