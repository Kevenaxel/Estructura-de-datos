# Modifica el algoritmo de burbuja para ordenar una lista de diccionarios de estudiantes por nota, por ejemplo:



def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n  - 1 -i):
            if lista[j]["Notas"]> lista[j+1]["Notas"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista


alumnos = [
    {"Nombre": "Ana", "Notas": 8.5},
    {"Nombre": "Brayan", "Notas": 9.0},
    {"Nombre": "Enmanuel", "Notas": 10.0}
]

ordenados = burbuja(alumnos)
print("Lista Ordenada:", ordenados)