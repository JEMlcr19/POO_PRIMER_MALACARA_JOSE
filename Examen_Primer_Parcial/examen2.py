
while True: 
    print("1. Calcular area Cuadrado")
    print("2. Calcular area Triangulo")
    print("3. Calcular area Rectangulo")
    print("4. Salir del programa")

    opcion = int(input("Ingresa el número de la opción que deseas realizar: "))

    if opcion == 4:
        print("¡Haz salido del programa!")
        break
    elif opcion == 1:
        num1 = int(input("Dame el primer lado: "))
        num2 = int(input("Dame el segundo lado: "))
        cuadrado = num1 * num2
        print("El area del cuadrado es:",cuadrado, "mts^2")
    
    elif opcion == 2:
        num1 = int(input("Dame el primer lado: "))
        num2 = int(input("Dame el segundo lado: "))
        rectangulo = num1 * num2
        print("El area del rectangulo es:",rectangulo, "mts^2")
    elif opcion == 3:
        num1 = int(input("Dame la altura del triángulo: "))
        num2 = int(input("Dame la base del triángulo: "))
        triangulo = (num1 * num2) / 2
        print("El area del triángulo es:",triangulo, "mts^2")