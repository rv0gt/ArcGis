import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit Titel
st.title('Interaktiver Plot der Funktion a + b*x + c*x^2')

# Slider für die Parameter a, b, c
a = st.slider('Wähle den Wert für a:', min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider('Wähle den Wert für b:', min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
c = st.slider('Wähle den Wert für c:', min_value=-10.0, max_value=10.0, value=3.0, step=0.1)

# Wertebereich für x erstellen (von 0 bis 10)
x = np.linspace(0, 10, 200)

# Funktion berechnen
y = a + b * x + c * x**2

# Plot erstellen
fig, ax = plt.subplots()
ax.plot(x, y, label=f'{a} + {b}x + {c}x^2')
ax.set_title('Plot der Funktion a + b*x + c*x^2')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True)

# Plot in Streamlit anzeigen
st.pyplot(fig)
