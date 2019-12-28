"Un postulante a un empleo, realiza un test de capacitacion, se obtuvo la"
"siguente informaion: cantidad total de preguntas que se realizaron y la"
"cantidad de preguntas que contesto correctamente. Se pide confeccionar y un"
"programa que ingrese los dos datos por teclado e informe el nivel del mismo"
"segun el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:"
"Nivel maximo: porcentaje>=90%"
"Nivel medio: porcentaje>=75% y <90%"
"Nivel regular: porcentaje>=50% y <75%"
"Fuera de Nivel: porcentaje<50%"

totalpreguntas=int(input("Ingrese la cantidad total de preguntas del examen: "))
totalcorrectas=int(input("Ingrese la cantidad total de preguntas contstadas correctamente: "))
porcentaje=totalcorrectas * 100 / totalpreguntas
if porcentaje>=90:
    print("Nivel maximo")
else:
    if porcentaje>=75:
        print("Nivel medio")
    else:
        if porcentaje>=50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
            
