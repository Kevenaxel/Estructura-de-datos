## La lista debe estar ordenada alfabeticamente y el programa debe indicar si el nombre esta o no registrado y en que posicion esta:
## Ana, Carlos, David, Esteban, Luisa, Maria, Sofia


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
    
numeros = ["Ana", "Carlos", "David", "Esteban", "Luisa", "Maria", "Sofia"]

valor_buscado = "Carlos"

resultado = busqueda_recursiva(numeros, valor_buscado, 0, len(numeros))

if resultado != -1:
    print(f"La persona{valor_buscado} esta en la posicion {resultado}")
else:
    print(f"El nombre {valor_buscado} no se encuentra en la lista")