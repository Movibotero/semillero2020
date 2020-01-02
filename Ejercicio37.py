"Realizar un programa que permita cargar dos listas de 15 valores cada una."
"Informar con un mensaje cual de las dos listas tine un valor acumulado mayor"
"(Mensajes (Lista 1 mayor), (lista 2 mayor), (listas iguales), tener en cuenta"
"que puede haber dos o mas estructuras repetitivas en el algoritmo"

x=1
suma1=0
suma2=0
print("primer lista")
while x<=15:
    valor=int(input("Ingrese el valor de esta lista: "))
    suma1=suma1+valor
    x=x+1
print("Segunda lista")
x=1
while x<=15:
    valor=int(input("Ingrese el valor de esta lista: "))
    suma2=suma2+valor
    x=x+1
if suma1>suma2:
    print("lista 1 mayor")
else:
    if suma2>suma1:
        print("Lista 2 mayor")
    else:
         print("Listas iguales")
            
