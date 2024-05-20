print("Para calcular el costo de envío de su producto, denos la siguiente información")
print("Ponga el producto en la báscula")
peso = float(input("El peso de su producto es: "))

if peso <= 1:
    print("Su tarifa es $50")
elif peso <= 5:
    print("Su tarifa es $100")
elif peso <= 10:
    print("Su tarifa es $200")
else:
    print("Su tarifa es $500")