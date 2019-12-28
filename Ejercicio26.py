"De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar"
"un programa que lea los datos de entrada e informe:"
"a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años"
"otorgarle un aumento del 20 %, mostrar el sueldo a pagar."
"b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,"
"otorgarle un aumento de 5 %."
"c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios."

sueldo=int(input("Ingrese el salario: "))
añosantiguedad=int(input("Ingrese los años de antiguedad: "))
if sueldo<500 and añosantiguedad>=10:
    print("Aumento del 20%")
    aumento1=sueldo * 0.20
    sueldopago=sueldo+aumento1
    print("Este es el sueldo a pagar con el aumento")
    print(sueldopago)
else:
    if sueldo<500 and añosantiguedad<10:
        aumento2=sueldo * 0.05
        sueldopago2=sueldo+aumento2
        print("Este es el sueldo a pagar con el aumento")
        print(sueldopago2)
    else:
        if sueldo>500:
            print("Este es el sueldo a pagar")
            print (sueldo)
