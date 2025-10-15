class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conexiones = {}
    
    def incluirVecino(self, vecino, peso=0):
        self.conexiones[vecino] = peso

    def verConexiones(self):
        return self.conexiones.keys()
    
    def verId(self):
        return self.id
    
    def verPeso(self, vecino):
        return self.conexiones[vecino]
    
    def __str__(self):
        return str(self.id) + "--> " + str([x for x in self.verConexiones()])
    
class Grafo:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
    
    def incluirVertice(self, clave):
        nuevoVertice = Vertice(clave)
        self.vertices[clave] = nuevoVertice
        self.numVertices += 1
        return nuevoVertice
    
    def verVertice(self, clave):
        return self.vertices.get(clave, None)
    
    def incluirArista(self, origen, destino, peso=0):
        if origen not in self.vertices:
            self.incluirVertice(origen)
        if destino not in self.vertices:
            self.incluirVertice(destino)

        self.vertices[origen].incluirVecino(destino, peso)

    def verListaVertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices.values())
    

grafo = Grafo()

grafo.incluirVertice(1)
grafo.incluirVertice(2)
grafo.incluirVertice(3)
grafo.incluirVertice(4)

print("Lista de Vertices: ", list(grafo.verListaVertices()))


grafo.incluirArista(1, 2, 4)
grafo.incluirArista(1, 4, 2)
grafo.incluirArista(2, 4, 1)
grafo.incluirArista(2, 3, 1)

print("\n Conexiones de Grafos(Diagrama): ")
for vertice in grafo:
    for vecino, peso in vertice.conexiones.items():
        print(f"{vertice.verId()} --- Peso: ({peso}) conectado ---> {vecino}")