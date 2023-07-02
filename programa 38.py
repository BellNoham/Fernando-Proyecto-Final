"Programa 38. Calcula la suma de numeros pares /n:"

def sumar_numeros_pares(feg):
    suma = 0
    for i in range(1,feg+1):
        if i % 2 == 0:
            suma += i
    return suma

solucion = sumar_numeros_pares(20)
print(solucion)

print(" /n Final del Programa")

