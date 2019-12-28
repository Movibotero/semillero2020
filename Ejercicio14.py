"Confeccionar un programa que pida por teclado tres notas de un alumno"
"calcule el promedio e imprima alguno de estos mensajes"
"promedio >7 promocionado, promedio >=4 y <7 regular, promedio <4 reprobado"

nota1=int(input("Ingrese la primer nota:"))
nota2=int(input("Ingrese la segunda nota:"))
nota3=int(input("Ingrese la tercer nota:"))
promedio=(nota1+nota2+nota3)/3
if promedio>=7:
    print("promocionado")
else:
    if promedio>=4:
        print("Regular")
    else:
         print("Reprobado")
            
