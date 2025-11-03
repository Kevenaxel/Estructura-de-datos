##Dada la lista ordenada [3, 5, 8, 12, 15, 20, 25, 30]
##Buscar el numero 15 utilizando busqueda binaria

def busqueda_binaria(lista,valor):
    inicio =0
    fin=len(lista)-1
    
    while inicio<=fin:
        medio =(inicio+fin)//2
        print(f"Comprando con {lista}.....")
         
        if lista[medio]==valor:
            return medio
        elif valor <lista[medio]:
            fin = medio -1
        else:
            inicio = medio+1
    
   
        
    return - 1



numeros = [3,5,8,12,20,25,30]\

resultado = busqueda_binaria(numeros,30)
if resultado !=-1:
    print(f"Numero encontrado esta en la posicion {resultado}")
else:
    print("El numero no fue encontrado")