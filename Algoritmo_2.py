import numpy as np
import time

def dfs_knapsack(items, W):
    n = len(items)
    max_profit = 0
    stack = [(0, 0, 0)]
    while stack:
        i, profit, weight = stack.pop()
        if weight > W:
            continue
        if i == n:
            max_profit = max(max_profit, profit)
            continue
        v, w = items[i]
        stack.append((i+1, profit+v, weight+w))
        stack.append((i+1, profit, weight))
    return max_profit

instancias = ["f1_l-d_kp_10_269.txt", "f2_l-d_kp_20_878.txt", "f3_l-d_kp_4_20.txt", "f4_l-d_kp_4_11.txt", "f5_l-d_kp_15_375.txt", "f6_l-d_kp_10_60.txt", "f7_l-d_kp_7_50.txt", "f8_l-d_kp_23_10000.txt", "f9_l-d_kp_5_80.txt", "f10_l-d_kp_20_879.txt"]
valores_optimos = ["f1_l-d_kp_10_269_vo.txt", "f2_l-d_kp_20_878_vo.txt", "f3_l-d_kp_4_20_vo.txt", "f4_l-d_kp_4_11_vo.txt", "f5_l-d_kp_15_375_vo.txt", "f6_l-d_kp_10_60_vo.txt", "f7_l-d_kp_7_50_vo.txt", "f8_l-d_kp_23_10000_vo.txt", "f9_l-d_kp_5_80_vo.txt", "f10_l-d_kp_20_879_vo.txt"]

for instancia, valor_optimo in zip(instancias, valores_optimos):
    # Lectura de la instancia
    with open(instancia, "r") as f:
        # Lectura de la primera línea
        linea = f.readline().strip().split()
        n = int(linea[0])
        w_max = int(linea[1])
        items = []

        # Lectura de las líneas con los valores de los items
        for _ in range(n):
            linea = f.readline().strip().split()
            v = int(float(linea[0]))
            w = int(float(linea[1]))
            items.append((v, w))

    # Lectura del valor óptimo
    with open(valor_optimo, "r") as f:
        valor_optimo = float(f.readline().strip().replace(',', '.'))

    # Llamado a la función del algoritmo
    inicio = time.time()  # Tiempo de inicio
    valor_obtenido = dfs_knapsack(items, w_max)
    fin = time.time()  # Tiempo de fin

    # Calcula la diferencia entre el valor obtenido y el valor óptimo
    diferencia = abs(int(valor_optimo) - int(valor_obtenido))

    # Comprueba si la solución es óptima
    es_optima = "La solución es óptima." if diferencia == 0 else ""

    # Obtiene la lista de elementos incluidos en la solución
    solucion = [i for i in range(n) if items[i][1] <= w_max]

    tiempo_ejecucion = fin - inicio  # Tiempo de ejecución

    # Impresión de los resultados
    print("Tiempo de ejecución: {:.3f} segundos".format(tiempo_ejecucion))
    print("Instancia: {}".format(instancia))
    print("Mejor valor encontrado: {}".format(valor_obtenido))
    print("Mejor solución encontrada: {}".format(solucion))
    print("Valor óptimo: {}".format(int(valor_optimo)))
    print("Diferencia: {:d}".format(diferencia))
    if diferencia == 0:
        print("La solución es óptima.")
    else:
        print("La solución no es óptima.")
    
    print("-----------------------")

