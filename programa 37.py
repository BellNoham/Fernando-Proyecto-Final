" Programa 37. Proyecto en Clases /n:"

value = 1
while value <= 5:
    print(value)
    value += 1
    print("Programa que indica cual de los tres valores es mayor")
    
    a = float(input("escriba el valor: "))
    b = float(input("escriba el valor: "))
    c = float(input("escriba el valor: "))
    
    if a > b and a > c:
        print("el numero mayor es a = ", a)
    
    if b > a and b > c:
        print("el numero mayor es b = ", b)
        
    if c > a and c > b:
        print("el numero mayor es c = ", c)
    
print(" /n Final del Programa")
        