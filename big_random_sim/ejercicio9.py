import numpy as np
cantidad_molec = 10000
alto = 10
ancho = 5
n_steps=300
wall_length=-alto+10
vel = .1

def moleculas(ancho,alto,cantidad_molec,n_steps,wall_length,vel,der=True):
    # Vamos a limtar las posiciones iniciales a posiciones con 1 solo digito decimal.
    # Con esto podemos agregar una performance significativa en el calculo de colisiones en las paredes.
    stats = []
    l = []
    aa = np.random.random((cantidad_molec, 1)) * (ancho - .21) +.1
    bb = np.random.random((cantidad_molec, 1)) * (2 * (alto-.2)) - (alto-.2)
    particulas = [aa*(2*der-1), bb]
    #particulas = [np.random.randint(1//vel,ancho*1//vel,(cantidad_molec,1))*vel*(der*2-1),np.random.randint(-alto*1//vel,alto*1//vel,(cantidad_molec,1))*vel]
    particulas = np.concatenate(particulas,-1)
    #veo que no haya nada sobre la pared
    assert(((particulas[:,0]<0.1)*(particulas[:,0]>-0.1)*(particulas[:,1]<=wall_length)).sum()==0)
    for i in range(n_steps):
        r = np.random.randint(0, 2, (cantidad_molec, 1))
        move = np.concatenate([r,abs(r-1)],-1)*(np.random.randint(0,2,(cantidad_molec,1))*2-1)*vel

        #Predigo el siguiente movimiento
        tmp = particulas+move
        pos = (tmp[:, 0] == 0) * (tmp[:, 1] <= wall_length)
        #Veo si estoy sobre la pared
        colision_recipiente = (tmp[:,0]<0.1)*(tmp[:,0]>-0.1)*(tmp[:,1]<=wall_length)
        #ancho
        colision_recipiente = colision_recipiente | (tmp[:, 0] >= ancho) | (tmp[:, 0] <= -ancho)
        #alto
        colision_recipiente = colision_recipiente | (tmp[:, 1] >= alto) | (tmp[:, 1] <= -alto)
        tmp = particulas + move * (1-colision_recipiente)[:, None]
        # CHECK FOR WALL
        assert(((tmp[:,0]<0.1)*(tmp[:,0]>-0.1)*(tmp[:,1]<=wall_length)).sum()==0)
        particulas = tmp
        #Finalmente esta correcto y actualizamos
        stats.append([(particulas[:,0]>0).sum(),(particulas[:,0]<=0).sum()] )
        l.append(particulas.reshape(1,-1,2))
    return l,stats

#Simulo las particulas de la derecha
l1,s1 = moleculas(ancho,alto,cantidad_molec,n_steps,wall_length,vel)
#Simulo las particulas de la izquierda
l2,s2 = moleculas(ancho,alto,cantidad_molec,n_steps,wall_length,vel,der=False)

a0,b0 = s1[0]
xt,y1,y2=[],[],[]

for i,(a,b) in enumerate(s1[1:]):
    xt.append(i)
    y1.append( a)
    y2.append( b)
    a0=a
    b0=b
import matplotlib.pyplot as plt
#ax = plt.plot(xt,y1)
#ax = plt.plot(xt,y2)
#print(xt,y1)
#plt.show()
from sim.drawer import DrawSimulation

l1 = np.concatenate(l1, axis=0)
l2 = np.concatenate(l2, axis=0)
DrawSimulation(l1, l2, ancho, alto, n_steps, 4, wall_length).draw("ejemplo.gif")



