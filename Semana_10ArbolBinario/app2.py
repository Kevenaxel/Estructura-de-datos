from collections import deque


d =deque()

d.append("Tarea 1")
d.append("Tarea 2")
d.appendleft("Tarea Urgente")


print("Cola actual de tareas: ", d)


print("Atendendiendo: ", d.popleft())
print("Atendendiendo: ", d.pop())

print("Cola con tareas: ",d)