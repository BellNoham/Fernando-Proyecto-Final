"Programa 39. Calcula el area de un triangulo /n:"

def calcular_area_triangulo(base,altura):
    area = (base*altura) / 2
    return area

base = float(input("escriba la base: "))
altura = float(input("escribe la altura: "))

area = calcular_area_triangulo(base, altura)

print("el area del triangulo es" , area)

print(" /n Fin del Programa")

    