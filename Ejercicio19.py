"Confeccionar un programa que lea pr teclado tres numeros"
"enteros distintos y nos muestre el mayor"

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
num3=int(input("Ingrese el tercer valor: "))
print("El mayor valor de los tres es: ")
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
