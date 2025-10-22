def factorial(n):
    if n == 0 or n ==1: #Caso Base
        return 1
    else:
        return n * factorial(n - 1) #  Caso recursivo
    
# Ejemplo de uso
print(f"5! = {factorial(5)}")