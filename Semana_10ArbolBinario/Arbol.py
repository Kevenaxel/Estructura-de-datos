## Arbol Binario accediendo desde la raiz
class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.izq = None
        self.der = None
        
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)
raiz.izq.der.izq = Nodo(8)
raiz.der.der.izq = Nodo(9)
raiz.der.der.der = Nodo(10)

print("Raiz:", raiz.valor) #Imprime el 1
print("Raiz:", raiz.izq.valor) #Imprime el 2
print("Raiz:", raiz.der.valor) #Imprime el 3
print("raiz:", raiz.izq.der.valor) #Imprimi el 5
print("Raiz:", raiz.izq.der.izq.valor) #Imprime el 8