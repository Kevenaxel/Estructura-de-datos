## Eres desarrollador de una plataforma de cursos en linea.
## Al Final


def heap(arr,n,i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2
    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heap(arr, n, mayor)

def heapshort(arr):
    n=len(arr)

    for i in range (n//2-1,-1,-1):
        heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heap(arr,i,0)
calificaciones=[78,55,92,30,60,45]
print("lista oiriginal:",calificaciones)
heapshort(calificaciones)
print("lista ordenada:",calificaciones)