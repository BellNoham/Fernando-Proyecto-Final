print("Programa 13. Programa que calcula el salario neto /n")

salario_bruto = float(input("ingresa su salario_bruto: "))

seguro_social = salario_bruto * 0.0975
print("el seguro_social es:", seguro_social)
round = (seguro_social,2)

seguro_educativo = salario_bruto * 0.0125
print("el seguro_educativo es:", seguro_educativo)
round = (seguro_educativo,2)

prestamo_personal = 50
print("el prestamo_personal es:", prestamo_personal)
round = (prestamo_personal,2)

salario_neto = salario_bruto - seguro_social - seguro_educativo - prestamo_personal

print("el salario neto es:", salario_neto)

print(" /n Final del Programa")
