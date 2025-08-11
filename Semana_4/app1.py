#crear un diccionario

estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "cursos": ["Python", "Estructura de datos"]
}

#Acceder a elementos
print (estudiante["nombre"])

#Agregar/Modificar
estudiante["edad"] = 22 
estudiante["carrera"] = "Ing. Software"

# Recorrer
for clave, valor in estudiante.items():
    print(clave, "=>", valor)