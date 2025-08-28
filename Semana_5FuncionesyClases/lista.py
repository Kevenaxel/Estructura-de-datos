#Se entregan 2 listas, verificar que elementos estan 
#Buscar([1,2,3,4,5,6], [6,3,2,3]) 1,5
#Buscar([1,2,3, 'hola'], [3.2])

def buscar(lista1, lista2):
    resultado = []
    
    for num in lista1:  #Si esta en lista1
        if num not in lista2:  #Y si no esta en lista2
            resultado.append(num)  #Mostrar Resultado num
            
            
    for num in lista2: #Si esta en lista2
        if num not in lista1: #Y si no esta en lista1
            resultado.append(num) #Mostrar Resultado num
        return resultado
    
#print (buscar([1,2,3,5,6], [6,3,2,3])) #1,5 Imprime los resultados

print (buscar([1,2,3, 'hola'], [3.2])) #Imprime Todo.
