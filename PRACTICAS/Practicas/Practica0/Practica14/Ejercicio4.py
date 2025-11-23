def bubble_sort_pasos(lista):
    n = len(lista)
    paso = 1

    for i in range(n):
        for j in range(0, n - i - 1):
            print(f"Paso {paso}: comparando {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j + 1]:
                print(" -> Se intercambian")
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                print(" -> No se intercambian")

            print("Lista actual:", lista)
            print("-" * 30)
            paso += 1

    return lista


numeros = [6, 2, 4]
bubble_sort_pasos(numeros)