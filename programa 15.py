print("Programa 15. Programa que ingresa los precio total de la compra con el impuesto incluido /n ")
precio1= float(input("precio del articulo1:"))
precio2 = float(input("precio del articulo2:"))
precio3 = float(input("precio del articulo3:"))

precio_del_articulo1 = precio1 * 1.07
precio_del_articulo2 =  precio2 * 1.07
precio_del_articulo3 =  precio3 * 1.07 

costototal = precio_del_articulo1 + precio_del_articulo2 + precio_del_articulo3

DR = round(costototal,2)

print("el costototal es de ", DR) 



