def busqueda(lista,valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

numeros = [8, 3, 10, 5, 2, 7]
buscado = 5

posicion = busqueda(numeros, buscado)
if posicion != -1:
    print(f"El Numero {buscado} Se encontro en la posicion {posicion}")
else:
    print(f"EL Numero {buscado} No se encontro en la lista")