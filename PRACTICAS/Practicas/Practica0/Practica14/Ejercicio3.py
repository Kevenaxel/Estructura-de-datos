def bubble_sort_descendente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:  # condición invertida
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


ejemplo = [10, 4, 7, 1, 9]
print(bubble_sort_descendente(ejemplo))