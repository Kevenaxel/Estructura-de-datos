##Un arbol Binario 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        
raiz = Nodo("A")
raiz.izq = Nodo("B")
raiz.der = Nodo("C")
raiz.izq.izq = Nodo("D")

def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end="")
        inorden(nodo.der)
        
        
print("Recorrido Inorden")
inorden(raiz)