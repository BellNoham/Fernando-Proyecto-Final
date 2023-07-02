print("Programa 31. /n:")
for x in range(1, 6):
    nota = input("escribe la nota"+ str(x))
    print(x)
    evaluacion = float(input("escriba la nota:"))
    
    if evaluacion >= 90 and evaluacion <= 100:
        print(" su evaluacion es A")
    
    elif evaluacion >= 80 and evaluacion <= 89:
        print(" su evaluacion es B")
    
    elif evaluacion >= 70 and evaluacion <= 79:
        print(" su evaluacion es C")
    
    elif evaluacion >= 60 and evaluacion <= 69:
        print(" su evaluacion es D")
    
    else:
        print(" su evaluacion es F")
    
print(" /n Final del programa")
    
    
    