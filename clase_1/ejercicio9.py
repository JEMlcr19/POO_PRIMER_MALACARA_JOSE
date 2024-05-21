contraseña = "POO123"
 
while True:
    intento = str(input("Escribe tu contraseña: "))
    if intento == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
    
