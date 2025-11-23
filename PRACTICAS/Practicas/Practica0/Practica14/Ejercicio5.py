def bubble_sort_strings(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].lower() > lista[j + 1].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


nombres = ["Pedro", "Ana", "maria", "Luis"]
print(bubble_sort_strings(nombres))