##Dada la lista  [15, 10, 23, 8, 12, 7, 30],
##Realiza una busqueda secuencial para encontrar el numero 12.
##Muestra la posicion si lo encuentra o un mensaje si no existe

datos = [15, 10, 23, 8, 12, 7, 30]
valor_buscado = 12
def buscar(lista, valor):
    for i in range(len(lista)):
        print(F"Comprando el {valor} con {lista[i]}")
        if lista[i] == valor:
            return i
    return  -1
resultado = buscar(datos, valor_buscado)
if resultado != -1:
    print(f"El Numero {valor_buscado} esta en la posicion {resultado}")
else:
    print(f"El Numero {valor_buscado} no se encuentra en la lista")