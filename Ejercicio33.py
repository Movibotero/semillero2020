"Se ingresa un conjunto de n alturas de personas por teclado. Mostras la"
"altura promedio de las personas"

n=int(input("Cantidad de personas: "))
x=1
suma=0
while x<=n:
    altura=float(input("Ingrese la altura de la persona: "))
    suma=suma+altura
    x=x+1
promedio=suma//n
print("Altura promedio")
print(promedio)
    
