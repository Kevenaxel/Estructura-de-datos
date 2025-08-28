# Ejercicio 4: Declara Variables de diferentes tipos de datos basicos y mostrar su informacion

# Declaracion de Variables
edad = 20       # Int
promedio = 8.5  # Float
nombre = "Juan" # String
activo = True   #bool

# Mostrar valor y tipo de cada variable usando Type()
print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f"Variable: nombre = {nombre}, Tipos: {type(nombre)}")
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

# Operaciones basicas entre variables compatibles
print("\n--- Operaciones Basicas ---")
print(f"Suma de edad + promedio = {edad + promedio}")               # int + float
print(f"Multiplicacion de edad * 2 = {edad * 2}")                   # int * int
print(f"Concatenacion de nombre + ' Perez ' = {nombre +  ' Perez '}")  # str + str
print(f"Negacion de activo = {not activo}")                         # Operacion Logica con bool
