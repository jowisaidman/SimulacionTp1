from random import random,choice,randint

class Particula():
    def __init__(self,alto,ancho,radio=0.1,color="r"):
        self.x,self.y = randint(-ancho*10,ancho*10)/10,randint(-alto*10,alto*10)/10
        self.vel = .1
        self.ancho = ancho
        self.color = color
        self.alto = alto
        self.radio = radio
        self.correct()

    def move(self):
        x,y = choice([[0,1],[1,0],[0,-1],[-1,0]])
        self.x += x * self.vel
        self.y += y * self.vel
        self.correct()

    def correct(self):
        if self.x >= self.ancho:
            self.x = self.ancho-self.radio
        if self.x <= -self.ancho:
            self.x = -(self.ancho-self.radio)

        if self.y >= self.alto:
            self.y = self.alto-self.radio
        if self.y <= -self.alto:
            self.y += -(self.alto-self.radio)
