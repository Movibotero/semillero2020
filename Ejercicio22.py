"Se ingresan tres valores por teclado, si todos son iguales se imprime la suma"
"del primero con el segundo y a este resultado se lo multiplica por el tercero"

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
num3=int(input("Ingrese el tercer valor: "))
if num1==num2 and num1==num3:
    suma=num1+num2
    print("La suma del primero con el segundo")
    print(suma)
    producto=suma*num3;
    print("Las suma del primero y el segundo multiplicado por el tercero")
    print(producto)
else:
    print("Los numeros no coinciden")
        
    
