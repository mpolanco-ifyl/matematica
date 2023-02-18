import streamlit as st
import numpy as np
from scipy.integrate import quad
from sympy import *
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora Matemática")

st.title("Calculadora Matemática")

st.header("Resolución de ecuaciones")
equation_key = 'equation' + str(np.random.randint(1000))
equation = st.text_input("Introduce una ecuación:", key=equation_key)
try:
    solution = solve(equation)
    st.write(f"Solución: {solution}")
except:
    pass

st.header("Cálculos numéricos")
number_key = 'number' + str(np.random.randint(1000))
number = st.number_input("Introduce un número:", value=0.0, key=number_key)
if st.button("Elevar al cuadrado"):
    result = np.square(number)
    st.write(f"{number} al cuadrado es {result}")

if st.button("Integrar x^2 de 0 a 1"):
    result, _ = quad(lambda x: x**2, 0, 1)
    st.write(f"La integral de x^2 de 0 a 1 es {result}")

st.header("Cálculos simbólicos")
symbol_key = 'symbol' + str(np.random.randint(1000))
x, y = symbols('x y')
equation = st.text_input("Introduce una ecuación:", key=symbol_key)
if st.button("Simplificar"):
    expression = simplify(equation)
    st.write(f"La expresión simplificada es {expression}")

st.header("Gráficos")
function_key = 'function' + str(np.random.randint(1000))
function = st.text_input("Introduce una función:", key=function_key)
try:
    x_values = np.linspace(-10, 10, 1000)
    y_values = [eval(function) for x in x_values]
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    st.pyplot(fig)
except:
    pass
