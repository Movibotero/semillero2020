"Ingrese por tecaldo un numero positivo de uno o dos digitos(1..99) mostrar"
"un mensaje indicando si el numero tiene uno o dos digitos (tener en cuenta que"
"condicion debe cumplir para tener dos digitos un numero entero"

num=int(input("Ingrese un un valor de 1 o 2 digitos: "))
if num<10:
    print("Tiene un digito")
else:
    print("Tiene dos digitos")
    
