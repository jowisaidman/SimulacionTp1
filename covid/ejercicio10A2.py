poblacion = 100
alto = 100
ancho = 100
porcentaje_contagios = .05
n_steps = 4000
DIST_CONTAGIO=2
vel = 1
import numpy as np
def inicializar(total,porcentaje_contagios):
    m = np.array([ancho-2,alto-2])
    b = -np.array([(ancho-2)//2,(alto-2)//2])
    enfermos = np.random.random((int(total*porcentaje_contagios),2)) *m+b
    sanos = np.random.random((total-int(total * porcentaje_contagios), 2))*m+b
    return enfermos,sanos

def contagiar(sanos, enfermos):
    # Todos con todos eje x
    x = (sanos[:,0][:, None] - enfermos[:,0]).reshape(-1)
    # Todos con todos eje y
    y = (sanos[:,1][:, None] - enfermos[:,1]).reshape(-1)
    # Distancia
    contagios = (x ** 2 + y ** 2) < DIST_CONTAGIO*DIST_CONTAGIO
    #Probailidad en caso de estar cerca
    contraerla = np.random.random(sanos.shape[0]*enfermos.shape[0])<=.6
    #ESTAS CERCA Y NO TE CUIDASTE
    contagios = contagios & contraerla
    #Si alguno de las personas te contagio entonces contagiado estas!
    return contagios.reshape(-1,enfermos.shape[0]).sum(-1)>0

def mover(vec):
    cantidad = vec.shape[0]
    r = np.random.randint(0, 2, (cantidad, 1))
    move = np.concatenate([r, abs(r - 1)], -1) * (np.random.randint(0, 2, (cantidad, 1)) * 2 - 1) * vel
    # Predigo el siguiente movimiento
    tmp = vec + move
    # ancho
    colision_recipiente = (tmp[:, 0] >= ancho//2) | (tmp[:, 0] <= -ancho//2)
    # alto
    colision_recipiente = colision_recipiente | (tmp[:, 1] >= alto//2) | (tmp[:, 1] <= -alto//2)
    tmp = vec + move * (1 - colision_recipiente)[:, None]
    return tmp

import matplotlib.pyplot as plt
def evolucion_infectados(t,sanos,enfermos,fname):
    fig, ax = plt.subplots()
    ax.plot(t, sanos, c='g')
    ax.plot(t, enfermos, c='r')
    ax.legend(['Sanos', 'Enfermos'])
    ax.set_title("Evolución de infectados")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Cantidad De Personas")
    plt.savefig("{}.png".format(fname))

#Sólo se mueven los individuos sanos.
#Una vez que un individuo sano se enferma, se mueve entre 10 y 20 turnos más
enfermos,sanos = inicializar(poblacion, porcentaje_contagios)
l1,l2 = [],[]
i = 0
l1.append(sanos.copy())
l2.append(enfermos.copy())
ice = np.zeros(enfermos.shape[0])
evo =[[],[],[]]
while sanos.shape[0]!=0 and i<n_steps:
    ice = np.clip(ice-1,0,20)
    i+=1
    #Calcular contagio
    if sanos.shape[0]!=0:
        idx = contagiar(sanos,enfermos)
        enfermos = np.concatenate([enfermos,sanos[idx]],axis=0)
        ice = np.concatenate([ice,np.random.randint(10, 21, idx.sum())])
        sanos = sanos[~idx]
    l1.append(sanos.copy())
    l2.append(enfermos.copy())

    #data graficos
    evo[0].append(i)
    evo[1].append(sanos.shape[0])
    evo[2].append(enfermos.shape[0])
    #Mover a todos
    if sanos.shape[0] != 0:
        sanos = mover(sanos)
    if sanos.shape[0] != 0:
        tmp_enfermos = mover(enfermos)
        enfermos[ice!=0] = tmp_enfermos[ice!=0]


from sim.drawer import DrawSimulation
DrawSimulation(l1[:300], l2[:300], ancho//2, alto//2, 300, 4, -alto//2).draw("covidA2.gif")
evolucion_infectados(evo[0],evo[1],evo[2],"evolucionA2")