##Soporta Operaciones
##append(x) ==> Agrega al Final
##appendleft(x) ==> Agrega al inicio
##pop() ==> Elimina del final
##popleft() ==> Elimina del Inicio

from collections import deque

d= deque()

d.append("Tarea 1")
d.append("Tarea 2")
d.appendleft("Tarea Urgente")

print("Cola Actual de Tareas  ", d)

print("Atendiendo: ", d.popleft())
print("Atendiendo: ", d.pop())

print("Cola con Tareas: ", d)
