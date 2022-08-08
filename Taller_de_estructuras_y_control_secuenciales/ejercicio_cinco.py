from re import A


nota_uno=float(input("ingrese el valor de la nota parcial uno: "))
nota_dos=float(input("ingrese el valor de la nota parcial dos: "))
nota_tres=float(input("ingrese el valor de la nota parcial tres: "))
nota_examen=float(input("ingrese la nota del examen: : "))
trabajo_final=float(input("ingrese nota del trabajo final: "))
promedio_parcial=nota_uno+nota_dos+nota_tres/3
calificacion_final=((nota_examen*30)+(trabajo_final*15)+(promedio_parcial*55))/100
print(f"su calificacion final es {calificacion_final} ")
