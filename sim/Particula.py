from random import randint

class Particula():
    def __init__(self,alto,ancho,matrix):
        self.x,self.y = randint(-ancho,ancho),randint(-alto,alto)
        self.vel = .1
        print(self.vel,self.x,self.y)
        self.ancho = ancho
        self.alto = alto
        self.radio=.2
        self.correct()
        self.matrix = matrix

    def move(self):
        self.matrix[]

    def correct(self):
        if self.x == self.ancho:
            self.x-=self.radio
        if self.x == -self.ancho:
            self.x += self.radio

        if self.y == self.alto:
            self.y -= self.radio
        if self.y == -self.alto:
            self.y += self.radio


Particula(10,10)
