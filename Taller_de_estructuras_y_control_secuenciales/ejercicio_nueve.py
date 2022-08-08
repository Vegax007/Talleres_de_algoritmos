horas_trabajadas=int(input("ingrese la cantidad de horas trabajadas: "))
precio_hora=float(input("ingrese el valor de cada hora: "))

sueldo=horas_trabajadas*precio_hora
descuento=sueldo*20/100
sueldo_neto=sueldo-descuento
print(f"el salario neto es de {sueldo_neto}")