def abstraccion():
    print("\nLa Abstracción es:")
    print("Es el proceso de ocultar los detalles complejos y mostrar solo la funcionalidad esencial.")
   
def encapsulamiento():
    print("\nEl Encapsulamiento es:")
    print("Es el principio de ocultar los datos y la implementación interna de un objeto, permitiendo el acceso solo a través de métodos públicos.")
    
def herencia():
    print("\nLa Herencia es:")
    print("Es el mecanismo que permite crear una nueva clase a partir de una clase existente, heredando sus atributos y métodos.")
    
def polimorfismo():
    print("\nEl Polimorfismoes:")
    print("Es el principio que permite que una función o método se comporte de manera diferente según el objeto que lo invoque.")
    
def mostrar_menu():
    while True:
        print("Menú:")
        print("1. Abstracción")
        print("2. Encapsulamiento")
        print("3. Herencia")
        print("4. Polimorfismo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            abstraccion()
        elif opcion == "2":
            encapsulamiento()
        elif opcion == "3":
            herencia()
        elif opcion == "4":
            polimorfismo()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.\n")

# Llamar al menú
mostrar_menu()