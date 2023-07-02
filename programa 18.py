"Programa 18. Calcular Interes Compuesto /n:"

Ci = float(input("escriba la capital inicial:"))
i = float(input("escriba la tasa de interes:"))
n = float(input("escriba el numero de periodos:"))

Cf = Ci * (1 + i) ** n
DR= round(Cf,2)

print("La capital Final es:", DR)

print("/n Final del Programa")