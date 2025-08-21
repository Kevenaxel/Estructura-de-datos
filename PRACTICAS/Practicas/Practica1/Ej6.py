# Ejercicio 6: Trabajar con listas de materias de Ingernieria de Software

# a) Crear Lista con 5 Materias
materias = ["Programacion", "Estructura de datos", "Base de Datos", "Ingenieria de Software", "Redes"]


# Mostrar la lista completa
print("Lista inicial de materia:", materias)


# b) Agregar 2 materias mas usando append()
materias.append("Sistemas Operativos")
materias.append("Inteligenica Artificial")
print("Lista despues de agregar 2 materias:", materias)

# C) Insertar una materia en la posicion 2 
materias.insert(2, "Matematicas Discretas")
print("Lista despues de insertar una materia en la posicion 2:", materias)

# d) Eliminar la ultima materia usando remove()
# Primero identificamos el nombre de la ultima materia
ultimas_materias = materias[-1]
materias.remove(ultimas_materias)
print("Lista despues de eliminar la ultima materia:", materias)

# e) Mostrar el numero total de materias
print("Numero total de materias:", len(materias))