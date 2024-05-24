while True:
    print("1. Grados C° a F°")
    print("2. Grados F° a C°")
    print("3. Salir")

    opcion = int(input("Selecciona la conversión que quieres realizar: "))

    if opcion == 3:
        print("¡Haz salido del programa!")
        break
    elif opcion == 1: 
        celsius1 = int(input("Ingresa los grados C°: "))
        farenheint = (celsius1*1.8) + 32
        print("Son", farenheint,"F°")

    elif opcion == 2:
        farenheint1 = int(input("Ingresa los grados F°: "))
        celsius = (farenheint1 - 32) / 1.8
        print("Son", celsius, "C°")
