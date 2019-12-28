"confeccionar un programa que permita cargar un numero entero positivo de"
"hasta tres cifras y muestre un mensaje indicando si tiene 1,2 o 3 cifras,"
"Mostrar un mensaje de error si el numero de cifras es mayor"

num=int(input("Ingrese un valor de hasta tes cifras: "))
if num<10:
    print("El numero es de una cifra:")
else:
    if num<100:
         print("El numero es de dos cifras:")
    else:
         if num<1000:
             print("El numero es de tres cifras:")
         else:
             print("Erros en la entrada de datos:")
