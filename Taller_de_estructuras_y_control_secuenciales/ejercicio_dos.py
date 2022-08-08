#supongamos que es interes compuesto

inversion=float(input("indique el capital a invertir: "))
duracion=int(input("escriba el numero de meses a calcular la inversion: "))
ganancia=inversion
for meses in range(duracion):
    inversion=meses*((ganancia*2)/100)
fondo_total=ganancia+inversion
print("el capital total obtenido es de: ", fondo_total)
