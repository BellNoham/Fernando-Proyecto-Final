print("Programa16. Juan esta cursando una materia en la universidad y necesita conocer cual sera su nota final en la asignatura /n")

c1 = float(input('ingrese la primera nota: '))
c2 = float(input('ingrese la segunda nota: '))
c3 = float(input('ingrese la tercera nota: '))
c4 = float(input('ingrese la cuarta nota: '))
c5 = float(input('ingrese la quinta nota: '))

NotaFinal = (c1 * 0.20) + (c2 * 0.15) + (c3 * 0.25) + (c4 * 0.10) + (c5 * 0.30)
DR = round(NotaFinal,2)

print("la nota final del estudiante es", DR)

print(" /n Final del Programa")