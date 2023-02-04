# Para el problema de los movimientos de caballo de ajedrez, se cumple que la
# relación que se da entre los los caminos que puede tomar el caballo es de grafo, 
# y el número de movimientos que puede tomar el caballo es igual a la longitud de 
# los caminos del grafo,por lo que se puede representar las distintas conexiones del 
# grafo en una matriz con 1 y 0, y el número de caminos que puede tomar el caballo es 
# igual a la suma de los elementos de la matriz elevada a la potencia n, siendo n la 
# cantidad de movimientos que puede tomar el caballo. 

import numpy as np

def main(n):
    M = np.matrix([[0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]])
    return np.sum(M**n)

if __name__ == "__main__":
    print(main(1))
    print(main(2))
    print(main(3))
    print(main(5))
    print(main(8))
    print(main(10))
    print(main(15))
    print(main(18))
    print(main(21))
    print(main(23))
    print(main(32))