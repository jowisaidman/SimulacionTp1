import matplotlib.pyplot as plt
SEMILLA = (99730+100866+96786+93762)//4

def GCL(n,Xo,incremento, modulo, multiplicador):
    """Recibe como parametro cinco enteros, numero de iteraciones n, semilla Xo,
    , incremnto, modulo y multiplicador. Imprime el valor de cada iteracion"""
    resultados = [Xo]
    for i in range(n):
        resultados.append((resultados[i]*multiplicador + incremento) % modulo)   
    resultados.pop(0)
    return resultados

def GCL_con_rango(n,Xo,incremento, modulo, multiplicador):
    """Recibe como parametro cinco enteros, numero de iteraciones n, semilla Xo,
    , incremnto, modulo y multiplicador. 
    Los numeros random generados estan entre 0 y 1.
    Imprime el valor de cada iteracion"""
    resultados = [Xo]
    for i in range(n):
        resultados.append(((resultados[i]*multiplicador + incremento) % modulo))  
    resultados.pop(0)
    for i in range(n):
        resultados[i] = resultados[i]/modulo   
    return resultados


print("Ejercicio 1 - Item A")
print(GCL(10,SEMILLA,1664525, 2**32, 1013904223))
print("#############################################")
print("Ejercicio 1 - Item B")
print(GCL_con_rango(10,SEMILLA,1664525, 2**32, 1013904223))
print("#############################################")
print("Ejercicio 1 - Item C")
plt.hist(GCL_con_rango(100000,SEMILLA,1664525, 2**32, 1013904223))
plt.show()
