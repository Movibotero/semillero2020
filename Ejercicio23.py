"Se ingresa por teclado tres numeros, si todos los valores ingresados son menores a 10"
"imprimir en pantalla la leyenda (Todos los numeros son menores que 10)"

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
num3=int(input("Ingrese el tercer valor: "))
if num1<10 and num2<10 and num3<10:
    print("Todos los numeros son menores a diez")
else:
    print("numeros mayores que 10")
