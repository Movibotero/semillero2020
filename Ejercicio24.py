"Se ingresa por teclado tres numeros, si almenos uno de los valores ingresados"
"es menor a 10,imprimir en pantalla la leyenda(algunos de los numero es menor a 10)"

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
num3=int(input("Ingrese el tercer valor: "))
if num1<10 or num2<10 or num3<10:
    print("Alguno de los numero es menor a 10")


