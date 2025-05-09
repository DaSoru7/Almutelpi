from CONTROLADORES.trabajadores import pedirNombre

nombre = input("Ingresa tu nombre ")
apellido = input("Ingresa tu apellido ")

pedirNombre(nombre, "nombre")
pedirNombre(apellido, "apellido")

print(nombre, " ", apellido)