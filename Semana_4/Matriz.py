#Imaginemos que tenemos una tabla de calificaciones de 3 estudiantes en 3 materias: Matematicas, Ciencia, Lenguaje

notas = [
    [8.5, 7.0, 9.0],
    [6.0, 8.5, 7.5],
    [9.0, 9.5, 8.0]
]
#Acceder a un elemento especifico
print("Nota del estudiante 2 en Ciencias:", notas[1][1])

#Recorrer la notas y mostrar todas las calificaciones 
for fila in notas:
    print (fila)

