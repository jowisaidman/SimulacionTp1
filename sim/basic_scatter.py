from drawer import DrawSimulation
from particula import Particula


ALTO=10
ANCHO=5
CANTIDAD_ITERACIONES= 3000
CANT_PART = 10000
ls = []

for _ in range(2):
    ps = [Particula(ALTO, ANCHO, 1) for _ in range(CANT_PART)]
    l = []
    for i in range(CANTIDAD_ITERACIONES):
        a,b = [],[]
        for p in ps:
            a.append(p.x)
            b.append(p.y)
            p.move()
        l.append([a, b])
    ls.append(l)

#DrawSimulation(*ls, ANCHO, ALTO, CANTIDAD_ITERACIONES, 4, 0).draw("ejemplo.gif")

#DrawSimulation(*ls, ANCHO, ALTO, CANTIDAD_ITERACIONES, 4, 0).draw("ejemplo.gif")

#DrawSimulation([[[0], [1]], [[0], [2]], [[0], [3]], [[0], [4]]], 5, 5, 4, 4,2).draw("ejemplo.gif")
