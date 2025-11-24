#Aplicar Quicksort para ordenar una lista de diccionarios de estudiantes por nota

#alumnos = [
#{"nombre": "Ana", "Nota": 8.5},
#{"nombre": "Luis", "Nota": 7.2},
#{"nombre": "Maria", "Nota": 9.0},
#]


def quicksort(alumnos):
    if len(alumnos) <= 1:
        return alumnos
    
    pivote = alumnos[0]["Nota"]
    
    menores = []
    iguales = []
    mayores = []
    
    for x in alumnos:
        if x["Nota"] < pivote:
            menores.append(x)
        elif x["Nota"] == pivote:
             iguales.append(x)
        else:
            mayores.append(x)
            
    return quicksort(menores) + iguales + quicksort(mayores)


def quicksort_desc(alumnos):
    if len(alumnos) <= 1:
        return alumnos
    
    pivote = alumnos[0]["Nota"]
    
    menores = []
    iguales = []
    mayores = []
    
    for x in alumnos:
        if x["Nota"] > pivote:
            mayores.append(x)
        elif x["Nota"] == pivote:
             iguales.append(x)
        else:
            menores.append(x)
            
    return quicksort_desc(mayores) + iguales + quicksort_desc(menores)



alumnos = [
  {"nombre": "Ana", "Nota": 8.5},
  {"nombre": "Luis", "Nota": 7.2},
  {"nombre": "Maria", "Nota": 9.0},
]

print("Lista Original:", alumnos)

ordenados_asc = quicksort(alumnos)
print("Ordenados de menor a mayor:", ordenados_asc)

ordenados_desc = quicksort_desc(alumnos)
print("Ordenados de mayor a menor:", ordenados_desc)

####    Kevin Mauricio Alvarenga Flores U20240632
