import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation, PillowWriter


class DrawSimulation():
    def __init__(self, puntos, ancho, alto,t,duracion,largo_pared):
        self.fig, self.ax = plt.subplots()
        self.ln1, = plt.plot([], [], 'ro')
        self.square, = plt.plot([], [])
        self.wall, = plt.plot([], [])

        plt.axis('off')
        #self.ln2, = plt.plot([], [], 'm*')
        self.alto = alto
        self.largo_pared=largo_pared
        self.ancho = ancho
        self.t = t
        self.puntos = puntos
        self.duracion = duracion #en segundos
        self.fps = t//duracion

    def draw(self,fname="ejemplo.gif"):
        ani = FuncAnimation(self.fig, self.update, [i for i in range(self.t)], init_func=self.init)
        writer = PillowWriter(fps=self.fps)
        ani.save(fname, writer=writer)
        os.system(f"start {fname}")

    def init(self):
        self.ax.set_xlim(-self.ancho-1,self.ancho+1)
        self.ax.set_ylim(-self.alto-1, self.alto+1)

    def update(self, i):
        self.square.set_data([-self.ancho,self.ancho,self.ancho,-self.ancho,-self.ancho], [-self.alto,-self.alto,self.alto,self.alto,-self.alto])
        self.wall.set_data([0,0],[self.alto-self.largo_pared, self.alto])
        self.ln1.set_data(self.puntos[i][0], self.puntos[i][1])