import time 

def torres_de_hanoi(n, origen, auxiliar, destino, movimiento):
    if n == 1:
        movimiento.append((origen, destino))
    else: 
        torres_de_hanoi(n-1, origen, destino, auxiliar, movimiento)
        movimiento.append((origen, destino))
        torres_de_hanoi(n-1, auxiliar, origen, destino, movimiento)
    return movimiento

def mostrar_torres(torres):
    print("Estado actual de las torres:")
    for nombre, torre in torres.items():
        print(f"{nombre}: {torre}")
    print("-" *30)

def jugar_hanoi():
    print("Reglas de la Torres de Hanoi")
    print("1- Solo se puede mover un disco a la vez")
    print("2- No se puede colocar un disco grande sobre uno pequeño")
    print("3- Debes de mover todos los disco de la torre A hacia la Torre C")

    n= int(input("Seleccione el numero de disco(Dificultad) 3 a 6: "))
    torres = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    solucion = torres_de_hanoi(n, 'A', 'B', 'C', [])
    tiempo_max = n * 25
    inicio = time.time()

    print(f"Tienes {tiempo_max} segundos")
    mostrar_torres(torres)

    movimientos_usuario = 0

    while torres['C'] != list(range(n, 0, -1)):
        if time.time() - inicio > tiempo_max:
            print("Se acabo su tiempo!")
            break

        movi = input("Movimiento (ejemplo: A C ) o 'salir :").upper()
        if movi == "SALIR":
            break

        if len(movi.split()) != 2:
            print("Formato invalido: Origen hacia el destino (Ejemplo: A C)")
            continue

        origen, destino = movi.split()

        if origen not in torres or destino not in torres:
            print("Torres son invalidades. Usemos A, B, C")
            continue

        if not torres[origen]:
            print("No hay discos en esta torre")
            continue

        disco = torres[origen][-1] 
        if torres[destino] and torres[destino][-1] < disco:
            print("Movimiento no permitido. no se puede poner un disco mas grande que el que se tiene")
            continue

        torres[destino].append(torres[origen].pop())
        movimientos_usuario += 1
        mostrar_torres(torres) 

        # Fin de juego
    print(" Resultado  ")
    if torres['C'] == list(range(n, 0, -1)):
        print(f"Felicidades lo lograste! Resolviste el juego en {movimientos_usuario} movimiento")
    else: 
        print("Sigue intentandolo")
        print(f"Solucion podria ser: ({len(solucion)} movimientos ): ")
        for i, (o, d) in enumerate(solucion, start=1):
            print(f"Paso {i}: mover de {o} a {d}")

if __name__ == "__main__":
    jugar_hanoi()