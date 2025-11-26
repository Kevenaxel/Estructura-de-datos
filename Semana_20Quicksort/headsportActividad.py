#Ejercicio: 
#Tu modulo se encarga de analizar los tiempos de entrega(en dias) de los pedidos realizados por los clientes.

#Para un informe de calidad de servicio, tu jefe te pide que ordenes los tiempos de entrega de menor a mayor
#para poder ver facilmente:
#Cuales pedidos llegaron mas rapido.
#Cuales tardaron mas.
#Si hay muchos pedidos con tiempos muy altos.
#Los tiempos de entrega de los ultimos 7 pedidos fueron:
#tiempos_Entrega = [5,2,7,3,10,4,6]

def heap(arr, n, i):

    mayor = i
    izquierda = 2 * i + 1
    derecha = 2* i + 2

    if izquierda < n and arr[izquierda] > arr[mayor]:
        mayor = izquierda
    if derecha < n and arr[derecha] > arr[mayor]:
        mayor = derecha
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heap(arr, n, mayor)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, - 1, -1):
        heap(arr, n, i)
    for i in range(n -1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)

tiempos_Entrega = [5,2,7,3,10,4,6]
def Orden_tiempos(tiempos):
    heapSort(tiempos)
    return tiempos

tiempos_Ordenados = Orden_tiempos(tiempos_Entrega)
print("Tiempos de entrega Ordenados de menor a mayor: ", tiempos_Ordenados)