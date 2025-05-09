from db import conexion

def validacionNombre(nombre): #Validacion del nombre
    print("2")
    caracteresProhibidos = ["@", "#", "$", "%", "&", "/", "!", "?", "="]
    for letra in nombre:
        if letra in caracteresProhibidos:
            return False
        
    if nombre and nombre.strip() and len(nombre)<= 30: #validacion de que el dato no este vacio y no sea mayor a 30 caracteres
        return True
    
    return False

def validacionColumna(campo):
    print("3")
    columna = ["nombre", "apellido"]
    if campo in columna:
        return True
    else:
        return False

def pedirNombre(nombre, campo): #Pide el nombre
    print("1")
    if validacionNombre(nombre) and validacionColumna(campo):
        ingresarNombreDb(nombre, campo)
        return True

def ingresarNombreDb(nombre, campo):
    try:
        print("4")
        conn = conexion()
        print("conexion terminada")
        cursor = conn.cursor()
        columna = campo
        print("ayayay")
        sql = f"INSERT INTO trabajadores({columna}) VALUES (%s)"
        print("ni aca?")
        cursor.execute(sql,(nombre,))
        print("no se a mandado")
        conn.commit()
        conn.close()
        print("Dato insertado correctamente")
        return True
    except Exception as e:
        print("Error al insertar en la base de datos", e)

