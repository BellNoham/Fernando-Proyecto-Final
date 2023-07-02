"Programa 21.  Calcule si una persona paga impuestos : \n"

sal = float(input(" Escriba el salario: "))

if sal <= 3000:
    i = sal * 1.07
    print("esta persona debe abonar", i)
else:
    print("no debe abonar impuestos")
    
print("\n Fin del programa")