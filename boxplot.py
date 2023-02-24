import matplotlib.pyplot as plt
import numpy as np

# Definimos los 10 tiempos que se van a comparar
tiempos = [0.000, 0.499, 0.000, 0.000, 0.016, 0.000, 0.000, 2.600, 0.000, 0.492]

# Boxplot
fig, ax = plt.subplots()
ax.boxplot(tiempos)
ax.set_xticklabels(["Tiempo"])
ax.set_ylabel("Tiempo (segundos)")
ax.set_title("Comparación de tiempos")
plt.show()