"Se carga una fecha (dia, mes y año) por teclado. Mostrar un mensaje si corresponde"
"al primer trimestre del año(enero, febrero o marzo).Cargar por teclado el valor"
"numerico del dia, mes y año"

dia=int(input("Ingrese el dia de nacimiento: "))
mes=int(input("Ingrese el numero del mes de nacimeinto: "))
año=int(input("Ingrese el año de nacimeinto: "))
if mes==1 or mes==2 or mes==3:
        print("Corresponde al primer trimestre")
else:
    print("Es de otro trimestre")
