
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App config
st.set_page_config(page_title="Mother's Day Heart", page_icon=":heart:", layout="centered")
st.title("💖 Happy Mother's Day 💖")

# Fixed message with names
header = "To: Wonderwoman, Best, Most Sacrificial, Coolest Mummy DS JS"
footer = "From: Your Dearest Baobei Gwen 💌"

# Show header
st.markdown(f"### {header}")

# Heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Plotting
fig, ax = plt.subplots()
ax.plot(x, y, color='red', linewidth=3)
ax.fill(x, y, color='lightcoral', alpha=0.6)
ax.text(0, -20, "You're the heart of our family!", fontsize=14, ha='center', color='darkred')
ax.axis('equal')
ax.axis('off')

# Show plot
st.pyplot(fig)

# Show footer
st.markdown(f"#### {footer}")
