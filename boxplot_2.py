import matplotlib.pyplot as plt
import numpy as np

# Tiempos de ejecución de los algoritmos
tiempo1 =  31.1292 # reemplaza con tu propio tiempo
tiempo2 =  3.616 # reemplaza con tu propio tiempo

# Boxplot
datos = [tiempo1, tiempo2]

fig2, ax2 = plt.subplots()
ax2.set_title('Comparación de tiempos de ejecución de algoritmos')
ax2.boxplot(datos)

# Agrega los ticks antes de las etiquetas
ax2.set_xticks([1, 2])
ax2.set_xticklabels(['Algoritmo 1', 'Algoritmo 2'])
ax2.set_ylabel('Tiempo de ejecución')

plt.show()
