print("Programa 14. Programa que calcula el costo total de una compra /n")
PG95 = input("escriba el precio de la gasolina:")
CLG = input("escriba la cantidad de litros:")

precio_de_gasolina = float(PG95)
cantidad_de_litros = float(CLG)

costo_sin_impuesto = precio_de_gasolina * cantidad_de_litros
costo_total = costo_sin_impuesto * 1.07

print("el costo total es de", round(costo_total,2))


print(" /n Final del Programa")