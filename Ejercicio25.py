"Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir"
"dos  valores enteros x e y (distintos a cero). Posteriormente imprimir en"
"pantalla en que cuadrante se ubica dicho punto.(1 cuadrante si x>0 Y y>0,"
"2 cuadrante: x<0 Y y>0, etc)"

x=int(input("Ingresar coordenada x: "))
y=int(input("Ingresar coordenada y: "))
if x>0 and y>0:
    print("Se encuentra en el cuadrante 1")
else:
    if x<0 and y>0:
        print("Se encuentra en el cuadrante 2")
    else:
        if x<0 and y<0:
            print("Se encuentra en el cuadrante 3")
        else:
            print("Se encuentra en el cuadrante 4")
        
        
