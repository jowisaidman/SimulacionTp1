import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation, PillowWriter


class DrawSimulation():
    def __init__(self, puntosr,puntosg, ancho, alto,t,duracion,largo_pared):
        self.fig, self.ax = plt.subplots()
        self.ln1, = plt.plot([], [], 'r.')
        self.ln2, = plt.plot([], [], 'g.')
        self.square, = plt.plot([], [])
        self.wall, = plt.plot([], [])

        plt.axis('off')
        #self.ln2, = plt.plot([], [], 'm*')
        self.alto = alto
        self.largo_pared=largo_pared
        self.ancho = ancho
        self.t = t
        self.puntosr = puntosr
        self.puntosg = puntosg
        self.duracion = duracion #en segundos
        self.fps = min(max(1, t//duracion), 30)

    def draw(self,fname="ejemplo.gif"):
        ani = FuncAnimation(self.fig, self.update, [i for i in range(self.t)], init_func=self.init)
        writer = PillowWriter(fps=self.fps)
        ani.save(fname, writer=writer)
        #os.system(f"start {fname}s")
        os.system(f"eog {fname}&")

    def init(self):
        self.ax.set_xlim(-self.ancho-1,self.ancho+1)
        self.ax.set_ylim(-self.alto-1, self.alto+1)

    def update(self, i):
        self.square.set_data([-self.ancho,self.ancho,self.ancho,-self.ancho,-self.ancho], [-self.alto,-self.alto,self.alto,self.alto,-self.alto])
        self.wall.set_data([0,0],[-self.alto, self.largo_pared])
        if len(self.puntosr)>i:
            self.ln1.set_data(self.puntosr[i][0], self.puntosr[i][1])
        if len(self.puntosg)>i:
            self.ln2.set_data(self.puntosg[i][0], self.puntosg[i][1])