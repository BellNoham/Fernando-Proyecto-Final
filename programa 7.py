print("Programa 7. Programa que calcula el volumen de un prisma rectangular /n")
i1 = input("escribir el valor del largo")
i2 = input("escribir el valor del ancho")
i3 = input("escribir el valor de la altura")

largo = float(i1)
ancho = float(i2)
altura = float(i3)

vol = (largo * ancho * altura)

volR = round(vol,4)

print("el volumen de un prisma rectangular " , volR)

print(" /n Final del Programa")