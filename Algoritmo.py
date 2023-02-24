import time

def mochila(pesos, valores, capacidad):
    n = len(pesos) # número de elementos
    mejor_valor = 0 # variable para almacenar el mejor valor encontrado
    mejor_solucion = [] # variable para almacenar la mejor solución encontrada
    
    # Iterar sobre todas las combinaciones de elementos posibles
    for i in range(2**n):
        solucion_actual = [] # variable para almacenar la solución actual
        peso_actual = 0 # variable para almacenar el peso actual
        valor_actual = 0 # variable para almacenar el valor actual
        
        # Convertir el índice de la iteración a binario y agregar ceros a la izquierda para que tenga longitud n
        binario = format(i, '0' + str(n) + 'b')
        
        # Verificar qué elementos están incluidos en la solución actual y calcular su peso y valor
        for j in range(n):
            if binario[j] == '1':
                solucion_actual.append(j)
                peso_actual += pesos[j]
                valor_actual += valores[j]
        
        # Verificar si la solución actual es mejor que la mejor solución encontrada hasta el momento
        if peso_actual <= capacidad and valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_solucion = solucion_actual
    
    return mejor_valor, mejor_solucion

instancias = ["f1_l-d_kp_10_269.txt", "f2_l-d_kp_20_878.txt", "f3_l-d_kp_4_20.txt", "f4_l-d_kp_4_11.txt", "f5_l-d_kp_15_375.txt", "f6_l-d_kp_10_60.txt", "f7_l-d_kp_7_50.txt", "f8_l-d_kp_23_10000.txt", "f9_l-d_kp_5_80.txt", "f10_l-d_kp_20_879.txt"]
valores_optimos = ["f1_l-d_kp_10_269_vo.txt", "f2_l-d_kp_20_878_vo.txt", "f3_l-d_kp_4_20_vo.txt", "f4_l-d_kp_4_11_vo.txt", "f5_l-d_kp_15_375_vo.txt", "f6_l-d_kp_10_60_vo.txt", "f7_l-d_kp_7_50_vo.txt", "f8_l-d_kp_23_10000_vo.txt", "f9_l-d_kp_5_80_vo.txt", "f10_l-d_kp_20_879_vo.txt"]

for instancia, valor_optimo in zip(instancias, valores_optimos):
    # Leer el archivo de la instancia y procesarla
    with open(instancia, 'r') as f:
        # Leer las primeras dos líneas del archivo
        n, capacidad = map(int, f.readline().split())

        # Crear listas para almacenar los pesos y valores de los elementos
        pesos = []
        valores = []

        # Leer el resto del archivo y agregar los pesos y valores a las listas correspondientes
        for linea in f.readlines():
            v, w = map(float, linea.strip().split())
            valores.append(v)
            pesos.append(w)

    # Calcular la mejor solución y su valor
    inicio = time.time()
    mejor_valor, mejor_solucion = mochila(pesos, valores, capacidad)
    tiempo_ejecucion= time.time()-inicio

    # Imprimir los resultados de la instancia
    print("Tiempo de ejecución:", round(tiempo_ejecucion, 4), "segundos")
    print("Instancia:", instancia)
    print("Mejor valor encontrado:", int(mejor_valor))
    print("Mejor solución encontrada:", mejor_solucion)

    # Leer el archivo de valores óptimos y obtener el valor óptimo correspondiente
    with open(valor_optimo, 'r') as f:
        valor_optimo_instancia = float(f.readline().replace(',', '.'))
       
    print("Valor óptimo:", int(valor_optimo_instancia))
    print("Diferencia:", int(valor_optimo_instancia - mejor_valor))
    
    # redondeamos la diferencia a 4 decimales
    diferencia_redondeada = round(abs(valor_optimo_instancia - mejor_valor), 4)
    
    # comprobamos si la solución encontrada es óptima
    if diferencia_redondeada <= 0.0001:
        print("La solución es óptima.")
    else:
        print("La solución no es óptima.")
        
    print("\n")

    # Cerrar los archivos
    f.close()