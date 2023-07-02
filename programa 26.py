"Programa 26. Clasificacion de Triangulos /n"

valorA = float(input("escriba el valor A:"))
valorB = float(input("escriba el valor B:"))
valorC = float(input("escriba el valor C:"))

if valorA == valorB == valorC:
    print("el triangulo es equilatero")

elif valorA == valorB or valorA == valorC or valorB == valorC:
    print("el triangulo es isoceles")

else:
    print("el triangulo es escaleno")
    
    
print(" /n Final del Programa")   