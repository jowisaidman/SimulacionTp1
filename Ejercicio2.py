import matplotlib.pyplot as plt
import random

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

def simular_dado(Xo):
    resultado_dado=GCL_con_rango(10,Xo,1664525, 2**32, 1013904223)[0]
    if ( 0<resultado_dado<=1/6 ):
        resultado_dado=1
    elif ( 1/6<resultado_dado<=2/6 ):
        resultado_dado=2
    elif ( 2/6<resultado_dado<=3/6 ):
        resultado_dado=3
    elif ( 3/6<resultado_dado<=4/6 ):
        resultado_dado=4
    elif ( 4/6<resultado_dado<=5/6 ):
        resultado_dado=5
    else:
        resultado_dado=6
    return resultado_dado


def simular_dados(n):
    tiradas=[]
    for i in range(1,n+1):
        tiradas.append((simular_dado(int(random.randrange(1000))),simular_dado(int(random.randrange(1000)))))
    return tiradas




print("Ejercicio 2 - Item A")
print("El espacio muestral es S={2,3,4,5,6,7,8,9,10,11,12}")
print("#############################################")
print("Ejercicio 2 - Item B")
print(simular_dados(10))
print("#############################################")
print("Ejercicio 1 - Item C")
#plt.hist(GCL_con_rango(100000,SEMILLA,1664525, 2**32, 1013904223))
#plt.show()
