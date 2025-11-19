# Ordenar las siguientes edades con metodo de Burbuja 5, 3, 8, 4, 2


def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n  - 1 -i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista

numeros = [5, 3, 8, 4, 2]
print("Lista original:", numeros)

ordenada = burbuja(numeros)
print("Lista ordenada:", ordenada)