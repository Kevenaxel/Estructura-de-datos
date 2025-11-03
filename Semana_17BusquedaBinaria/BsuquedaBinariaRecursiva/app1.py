## Funcion: busqueda_binaria_recurisva
## Objetivo: Buscar un valor dentro de una lista ORDENADA
## Utilizando recursividad

def busqueda_recursiva(lista, valor, inicio, fin):
    
    if inicio > fin:
        return -1
    
    
    medio = (inicio + fin)//2
    print(f"Comparando con {lista[medio]} -----" )
    
    if lista[medio]==valor:
        return medio
    elif valor < lista[medio]:
        return busqueda_recursiva(lista, valor, inicio, medio -1)
    else:
        return busqueda_recursiva(lista, valor, medio +1, fin)
    
numeros = [3,5,8,12,20,25,30]

valor_buscado = 20

resultado = busqueda_recursiva(numeros, valor_buscado, 0, len(numeros))

if resultado != -1:
    print(f"El numero {valor_buscado} esta en la posicion {resultado}")
else:
    print(f"El numero {valor_buscado} no se encuentra en la lista")