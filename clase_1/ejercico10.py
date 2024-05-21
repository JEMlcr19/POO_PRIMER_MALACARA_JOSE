respuesta = "n"
while True: 
    print("1. Hacer una suma")
    print("2. Salir del programa")

    opcion = int(input("Ingresa el número de la opción que deseas realizar: "))

    if opcion == 2:
        print("¡Haz salido del programa!")
        break

    num1 = float(input("Dame el primer número: "))
    num2 = float(input("Dame el segundo número: "))
    suma = num1 + num2
  
    print("La suma es:",suma)



