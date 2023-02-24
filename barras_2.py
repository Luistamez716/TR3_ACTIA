import matplotlib.pyplot as plt
import numpy as np

# Tiempos de ejecución de los algoritmos
tiempo1 =  31.1292 # reemplaza con tu propio tiempo
tiempo2 =  3.616 # reemplaza con tu propio tiempo

# Gráfica de barras
fig, ax = plt.subplots()
indice = np.arange(2)
ancho = 0.35

rects1 = ax.bar(indice, [tiempo1, tiempo2], ancho)

ax.set_ylabel('Tiempo de ejecución')
ax.set_title('Comparación de tiempos de ejecución de algoritmos')
ax.set_xticks(indice)
ax.set_xticklabels(('Algoritmo 1', 'Algoritmo 2'))

fig.tight_layout()

plt.show()