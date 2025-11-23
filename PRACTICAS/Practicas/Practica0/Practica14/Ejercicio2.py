def bubble_sort_optimizado(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False  # bandera

        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True

        if not intercambio:  
            break  # la lista ya está ordenada

    return lista


# Ejemplo
datos = [1, 2, 3, 4, 5]
print(bubble_sort_optimizado(datos))