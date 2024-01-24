import streamlit as st
from neurona import Neuron

st.image("./src/data/neurona.jpg")
st.title("Simulador de neurona")

index = st.slider("Elige un numero de entradas/pesos que tendrá la neurona", min_value=1, max_value=10)

st.subheader("Pesos")
# Columns_weights as an iterator
columns_weights = st.columns(index)
weight_values = []
for x in range(index):
    # Add the slider number amount of inputs to columns_weights
    # While also saving their values into weight_values
    weight_values.append(columns_weights[x].number_input(f"w$_{x}$",key=f"w{x}"))# _{} used for sibscript text
st.write(f"w = {weight_values}")

st.subheader("Entradas")
columns_entries = st.columns(index)
entries_values = []
for x in range(index):
    # Same process as in the weights sections
    entries_values.append(columns_entries[x].number_input(f"x$_{x}$", key=f"val{x}"))
st.write(f"x = {entries_values}")


s1,s2 = st.columns(2)

s1.subheader("Sesgo")
sesgo = s1.number_input("Introduce el valor del sesgo", key="sesgo")

s2.subheader("Función de activación")
func = s2.selectbox("Elige una función de activación",["ReLu","Sigmoid","tanh"])

if st.button("Calcular la salida"):
    # Declare the class everytime you push a button
    # It's the same as having the declaration outside since streamlit reloads
    # the whole page when interacting w a component
    n = Neuron(weight_values,sesgo,func)
    st.write(n.run(input_data=entries_values))