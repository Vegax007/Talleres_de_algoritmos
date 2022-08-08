from math import sqrt
a=float(input("ingrese el lado a: "))
b=float(input("ingrese el lado b: "))
c=float(input("ingrese el lado c: "))
s=(a+b+c)/2
area=sqrt( s*(s-a)*(s-b)*(s-c))
print(f"su area es: {area} ")
