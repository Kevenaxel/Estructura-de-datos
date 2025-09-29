class SocialNetwork:
    def __init__(self, id_user, name):
        self.id = id_user
        self.name = name
        self.left = None
        self.right = None

def insert(root, id_user, name):
    if root is None:
        return SocialNetwork(id_user, name)
    
    if id_user < root.id:
        root.left = insert(root.left, id_user, name)
    elif id_user > root.id:
        root.right = insert(root.right, id_user, name)
        
    return root

def search(root, id_user):
    if root is None or root.id == id_user:
        return root
    if id_user < root.id:
        return search(root.left, id_user)
    else:
        return search(root.right, id_user)
    
    
def inorder(root):
    if root:
        inorder(root.left)
        print(f"ID: {root.id}, Name: {root.name}")
        inorder(root.right)
        
def preorder(root):
    if root:
        print(f"ID: {root.id}, Name: {root.name}")
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"ID: {root.id}, Name: {root.name}")
        
def min_nodo(nodo):
    current = nodo
    while current.left:
        current = current.left
    return current
        
def delete(root, id_user):
    if root is None:
        return root
    if id_user < root.id:
        root.left = delete(root.left, id_user)
    elif id_user > root.id:
        root.right = delete(root.right, id_user)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_nodo(root.right)
        root.id = temp.id
        root.name = temp.name
        root.right = delete(root.right, temp.id)
    return root   
        
     
root = None
usuarios =[
    (50, "Alice"),
    (30, "Bob"),
    (70, "Charlie"),
    (20, "Diana"),
    (40, "Eve"),
    (60, "Frank"),
    (80, "Grace")
]

for id_user, name in usuarios:
    root = insert(root, id_user, name)
    
    
print("Inorder Traversal:")
inorder(root)       
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)

print("\n Buscar usuario con ID 40:")
result = search(root, 40)
if result:
    print(f"Encontrado el ID: {result.id},  Nombre: {result.name}")
else:
    print("Usuario no encontrado")
    
print("\n Eliminar un Usuario con ID 30")
root = delete(root, 30)

print("Recorrido actualizado inorder")
inorder(root)

