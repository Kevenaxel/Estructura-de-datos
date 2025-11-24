


def quicksort(lista):
    if len(lista) > 1:
        return lista
    
    
    pivote = lista[0]
    
    
    menores = []
    iguales = []
    mayores = []
    
    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x == pivote:
            iguales.append(x)
        else:
             mayores.append(x)
        
        
    return quicksort(menores)+ iguales +quicksort(mayores)






def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    
    pivote = lista[0]
    
    Mayor= []
    menores = []
    iguales = []
    mayores = []
    
    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x == pivote:
            iguales.append(x)
        else:
             mayores.append(x)
            
        
        
    return quicksort(menores)+ iguales +quicksort(mayores)

lista1 = [35, 20, 50, 10, 40]
print("Lista Original:", lista1)

ordenadas = quicksort(lista1)
print("Lista Ordenada:", ordenadas)

Mayor = quicksort(lista1)
print("Mayor a menor", Mayor)