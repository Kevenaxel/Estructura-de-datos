# Ejercicio 7: Lista de calificaciones y estadísticas

# Crear una lista con 8 calificaciones (0 a 10)
calificaciones = [8, 9, 7, 10, 6, 5, 9, 8]

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Calificación máxima y mínima
maxima = max(calificaciones)
minima = min(calificaciones)

# Contar cuántas calificaciones están por encima del promedio
mayores_promedio = sum(1 for nota in calificaciones if nota > promedio)

# Ordenar las calificaciones de mayor a menor
ordenadas = sorted(calificaciones, reverse=True)

# Mostrar resultados
print("=== Estadísticas del Estudiante ===")
print("Calificaciones:", calificaciones)
print(f"Promedio: {promedio:.2f}")
print(f"Calificación máxima: {maxima}")
print(f"Calificación mínima: {minima}")
print(f"Cantidad de calificaciones por encima del promedio: {mayores_promedio}")
print("Calificaciones ordenadas de mayor a menor:", ordenadas)