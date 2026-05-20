import streamlit as st
# Importamos exactamente el mismo motor
from validator import evaluar_transaccion

st.set_page_config(page_title="SentryBank Web Gateway")

st.title("SentryBank AI Web Gateway")
st.write("Detección de fraudes en entornos de producción mediante Machine Learning descentralizado.")
st.markdown("---")

# Formulario Web
st.header("1. Parámetros de la Operación")

col1, col2 = st.columns(2)
with col1:
    id_cliente = st.text_input("ID Cliente:", value="CLI-9948")
with col2:
    monto = st.number_input("Monto de la Transacción ($):",
                            min_value=0.0, value=150.00, step=10.0)

st.subheader("2. Variables de Comportamiento (Modelo IA)")
cant_fallidas = st.number_input(
    "Transacciones Fallidas (Últimos 7 días):", min_value=0, value=0, step=1)
risk_score = st.slider("Puntaje de Riesgo Interno (Risk Score):",
                       min_value=0.0, max_value=1.0, value=0.0, step=0.01)

st.markdown("---")

if st.button("AUDITAR TRANSACCIÓN WEB", type="primary"):
    if monto <= 0:
        st.warning("El monto debe ser estrictamente mayor a $0.00")
    elif monto > 50000:
        st.error(
            f"### RECHAZADA POR POLÍTICA BANCARIA\n\nEl monto de **${monto:,.2f}** excede el límite automático. Transacción enviada a auditoría manual por Lavado de Activos.")
    else:
        # LLAMADA AL MISMO MOTOR (validator.py)
        respuesta = evaluar_transaccion(cant_fallidas, risk_score)

        if respuesta["codigo"] == 1:
            st.error(
                f"### TRANSACCIÓN RECHAZADA\n\n**ID Cliente:** {id_cliente}\n\n**Motivo:** {respuesta['motivo']}")
        elif respuesta["codigo"] == 0:
            st.success(
                f"### TRANSACCIÓN APROBADA\n\n**ID Cliente:** {id_cliente}\n\n**Monto:** ${monto:,.2f}\n\n**Filtro IA:** {respuesta['motivo']}")
        else:
            st.info(f"Falla en el motor: {respuesta['motivo']}")
