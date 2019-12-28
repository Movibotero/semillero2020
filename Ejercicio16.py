"Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el"
"numero es positivo, negativo o nulo (es decir cero)"

num=int(input("Ingrese un valor: "))
if num==0:
    print("Se ingreso el cero")
else:
    if num>0:
        print("numero positivo")
    else:
         print("numero nulo o negativo")
            
