import streamlit as st

st.set_page_config(page_title="Calculadora de Precios", page_icon="💰")

st.title("💼 Calculadora de Precio de Venta")
st.markdown("Calculá tu precio ideal y margen de ganancia de forma rápida 🚀")

# Inputs
costo_fijo = st.number_input("💸 Costo fijo por unidad ($)", min_value=0.0, step=0.1)
costo_variable = st.number_input("🛠️ Costo variable por unidad ($)", min_value=0.0, step=0.1)
porcentaje_ganancia = st.number_input("📈 Margen deseado de ganancia (%)", min_value=0.0, step=0.1)

# Cálculos
costo_total = costo_fijo + costo_variable
precio_venta_sugerido = costo_total * (1 + porcentaje_ganancia / 100)
beneficio_neto = precio_venta_sugerido - costo_total

# Resultados
st.subheader("📊 Resultados")
st.write(f"**🧮 Costo total por unidad:** ${costo_total:.2f}")
st.write(f"**🏷️ Precio sugerido de venta:** ${precio_venta_sugerido:.2f}")

if beneficio_neto > 0:
    st.success(f"✅ Ganancia neta por unidad: ${beneficio_neto:.2f}")
elif beneficio_neto == 0:
    st.warning("⚖️ Estás en el **punto de equilibrio**.")
    st.markdown(
        "🔹 En este punto, el precio de venta **cubre exactamente todos los costos**.\n"
        "🔹 No ganás ni perdés dinero.\n"
        "🔹 Ideal para conocer cuánto debés cobrar **mínimo** para no tener pérdida."
    )
else:
    st.error(f"❌ Pérdida por unidad: ${beneficio_neto:.2f}")