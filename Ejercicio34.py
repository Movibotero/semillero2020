"En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar"
"un programa que lea los sueldos que cobra cada empelado e informe cuantos"
"empleados cobran en tre $100 y $300 y cuantos cobran mas de $300. Ademas el"
"programa debera informar el importe que gasta la empresa en sueldos a personal"

n=int(input("Ingrese el numero de empleados: "))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
    sueldo=int(input("Ingrese el sueldo del empleado: "))
    if sueldo<=300:
        conta1=conta1+1
    else:
        conta2=conta2+1
    gastos=gastos+sueldo
    x=x+1
print("Cantidad de empleados con sueldo entre 100 y 300")
print(conta1)
print("Cantidad de empleados con sueldo mayor a 300")
print(conta2)
print("Gastos total de la empresa en sueldos")
print(gastos)
    
