import numpy as np
cantidad_molec = 1
alto = 10
ancho = 5
n_steps=1000
wall_length=-alto
vel = .1

def moleculas(ancho,alto,n_steps,vel):
    l = []
    particulas = np.array([[0,0]])
    for i in range(n_steps):
        r = np.random.randint(0, 2, (1, 1))
        move = np.concatenate([r,abs(r-1)],-1)*(np.random.randint(0,2,(1,1))*2-1)*vel
        particulas = particulas+move
        l.append(particulas.reshape(1,-1,2))
    return l

l1 = moleculas(ancho,alto,n_steps,vel)

from sim.drawer import DrawSimulation
l1 = np.concatenate(l1,axis=0)
DrawSimulation(l1, [], ancho, alto, n_steps, 4, -alto).draw("one-particle.gif")



