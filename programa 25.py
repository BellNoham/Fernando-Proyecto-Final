"Programa 25. Calculadora de Descuentos /n "

PrecioDelProducto = float(input("Escriba el Precio del producto: "))
Descuento = float(input("Escriba el Porcentaje de descuento: "))

Descuento = (Descuento * PrecioDelProducto) / 100

PrecioFinal = PrecioDelProducto - Descuento 

DR = round(PrecioFinal,2)
print("El PrecioFinal es ", DR)

if PrecioFinal < 50:
     print("!Oferta Especial!")
     
print(" /n: Final del Programa")