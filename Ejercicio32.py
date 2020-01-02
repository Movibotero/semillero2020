"Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe"
"Cuantos tiene notas mayores o iguales a 7 y cuantos menores"

x=1
conta1=0
conta2=0
while x<=10:
    nota=int(input("Ingrese la nota del estudiante: "))
    if nota>=7:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1
print("Cantidad de alumnos con notas mayores o iguales a 7")
print(conta1)
print("Cantidad de alumnos con notas menores a 7")
print(conta2)
