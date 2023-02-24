import matplotlib.pyplot as plt
import numpy as np

# Definimos los 10 tiempos que se van a comparar
tiempos = [0.000, 0.499, 0.000, 0.000, 0.016, 0.000, 0.000, 2.600, 0.000, 0.492]

# Gráfica de barras
fig, ax = plt.subplots()
ax.bar(range(len(tiempos)), tiempos)
ax.set_xticks(range(len(tiempos)))
ax.set_xticklabels(["Tiempo " + str(i+1) for i in range(len(tiempos))])
ax.set_ylabel("Tiempo (segundos)")
ax.set_title("Comparación de tiempos")
plt.show()