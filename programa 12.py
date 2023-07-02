print("Programa 12. Programa que calcula el interes a pagar /n")

prestamo = float(input("Escriba el valor del prestamo:"))
tasa_anual = float(input("Escriba el valor de tasa_anual:"))
plazo_meses = float(input("Escriba el valor de plazo_meses:"))

tasa_decimal = tasa_anual / 100
plazo_anios = plazo_meses / 12
interes = prestamo * tasa_decimal * plazo_anios

DR = round(interes,2)

print("El interes a pagar es:", DR)

print(" /n Final del Programa")