class recorrido:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izq)
        preorden(nodo.der)
        
def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=" ")
        inorden(nodo.der)

def postorden(nodo):
    if nodo:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=" ")
        
## Creamos el Arbol

raiz = recorrido("A")
raiz.izq = recorrido("B")
raiz.der = recorrido("C")
raiz.izq.izq = recorrido("D")
raiz.izq.der = recorrido("E")
raiz.der.izq = recorrido("F")
raiz.der.der = recorrido("G")

print("Recorrido Preorden: ")
preorden(raiz)

## A B D E C F G 

print("Recorrido Inorden")
inorden(raiz)

## D B E A F C G 

print("Recorrido Postorden")
postorden(raiz)

## D E B F G C A