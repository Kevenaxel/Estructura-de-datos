class redSocial:
    def _init_(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

def insertar(raiz, id_usuario, nombre):
            if raiz is None:
                return redSocial(id_usuario, nombre)
            
            if id_usuario < raiz.id:
                raiz.izquierdo = insertar(raiz.izquierdo, id_usuario, nombre)
            if id_usuario > raiz.id:
                raiz.derecho = insertar(raiz.derecho, id_usuario, nombre)
            return raiz
def buscar(raiz, id_usuario):
    if raiz is None or raiz.id == id_usuario:
        return raiz
    if id_usuario < raiz.id:
        return buscar(raiz.izquierdo, id_usuario)
    else:
        return buscar(raiz.derecho, id_usuario)
    
def inorden(raiz):
    if raiz:
        inorden(raiz.izquierdo)
        print(f"ID:{raiz.id}, Nombre: {raiz.nombre}")
        inorden(raiz.derecho)
        
def preorder(raiz):
    if raiz:
        print(f"ID: {raiz.id}, Nombre: {raiz.nombre}")
        preorder(raiz.izquierdo)
        preorder(raiz.derecho)
        
def postorder(raiz):
    if raiz:
        postorder(raiz.izquierdo)
        postorder(raiz.derecho)
        print(f"ID: {raiz.id}, Nombre: {raiz.nombre}")
        
raiz = None

usuarios = [
    (50, "Ana"),
    (30, "Luis"),
    (70, "Maria"),
    (20, "Pedro"),
    (40, "Sofia"),
    (60, "Carlos"),
    (80, "Lucia")
]

for id_usuario, nombre in usuarios:
    raiz + insertar(raiz, id_usuario, nombre)
    
    print(inorden)