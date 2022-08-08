from importlib.util import decode_source


valor=float(input("ingrese el valor de la compra: "))
descuento = valor*15/100
valor_total = valor-descuento
print(f"valor total con el descuento incluido es de: {valor_total}")
