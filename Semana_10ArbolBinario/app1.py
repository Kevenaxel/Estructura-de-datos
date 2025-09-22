class Nodo :
    def init(self,valor):
        self.valor = valor
        self.izq = None
        self.der = None


raiz = Nodo("A")
raiz.izq = Nodo("B")         
raiz.der = Nodo("C")
raiz.izq.izq = Nodo("D") 

def  inorder(nodo):
    if nodo:
        inorder(nodo.izq)
        print(nodo.valor, end=" ")
        inorder(nodo.der)
        
print("Recorrido inorder:")
inorder(raiz)
