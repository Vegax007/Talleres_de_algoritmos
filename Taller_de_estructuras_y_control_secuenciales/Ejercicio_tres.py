sueldo_base=float(input("ingrese el valor de su sueldo base: "))
venta_uno=float(input("ingrese el valor de la venta uno: "))
venta_dos=float(input("ingrese el valor de la venta dos: "))
venta_tres=float(input("ingrese el valor de la venta tres: "))

sueldo_total=sueldo_base+((venta_uno*10/100)+(venta_dos*10/100)+(venta_tres*10/100))
#lo tome como que el empleado gana el 10% del valor de cada venta y no como el 10% de las ventas totales

print(f"el sueldo total que recibirá el empleado es de {sueldo_total}")
