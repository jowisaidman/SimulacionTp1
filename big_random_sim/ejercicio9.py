import numpy as np
cantidad_molec = 10000
alto = 10
ancho = 5
n_steps=3000
wall_length=-alto+10
vel = .1

def moleculas(ancho,alto,cantidad_molec,n_steps,wall_length,vel,der=True):
    stats = []
    l = []
    #empiezan en el 0.1 hasta
    particulas = [np.random.randint(1,ancho*1//vel,(cantidad_molec,1))*vel*(der*2-1),np.random.randint(-alto*1//vel,alto*1//vel,(cantidad_molec,1))*vel]
    particulas = np.concatenate(particulas,-1)
    #veo que no haya nada sobre la pared
    assert(((particulas[:,0]==0)*(particulas[:,1]<=wall_length)).sum()==0)
    r = np.random.randint(0, 2, (cantidad_molec, 1))
    move = np.concatenate([r, abs(r - 1)], -1) * (np.random.randint(0, 2, (cantidad_molec, 1)) * 2 - 1) * vel
    for i in range(n_steps):
        r = np.random.randint(0, 2, (cantidad_molec, 1))
        move = np.concatenate([r,abs(r-1)],-1)*(np.random.randint(0,2,(cantidad_molec,1))*2-1)*vel

        tmp = particulas+move
        pos = (tmp[:, 0] == 0) * (tmp[:, 1] <= wall_length)
        tmp = particulas+move*(1-(tmp[:,0]<0.1)*(tmp[:,0]>-0.1)*(tmp[:,1]<=wall_length))[:, None]
        # CHECK FOR WALL
        assert(((tmp[:,0]<0.1)*(tmp[:,0]>-0.1)*(tmp[:,1]<=wall_length)).sum()==0)

        tmp[:,0] = np.clip(tmp[:,0], -ancho+vel, ancho-vel)
        tmp[:, 1] = np.clip(tmp[:,1],-alto+2*vel,alto-vel)
        particulas = tmp
        stats.append([(particulas[:,0]>0).sum(),(particulas[:,0]<=0).sum()] )
        l.append([particulas[:,0],particulas[:,1]])
    return l,stats

l1,s1 = moleculas(ancho,alto,cantidad_molec,n_steps,wall_length,vel)
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
ax = plt.plot(xt,y1)
ax = plt.plot(xt,y2)
#print(xt,y1)
plt.show()
from sim.drawer import DrawSimulation
print("dibujando...")
#DrawSimulation(l1,l2, ancho, alto, n_steps, 4, wall_length).draw("ejemplo.gif")



