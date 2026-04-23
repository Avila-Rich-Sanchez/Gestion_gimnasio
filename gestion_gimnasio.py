import sqlite3
import os
import time

# Conectar base de datos (Si no existe se crea)
conection_bd = sqlite3.connect('BD_Clientes.db')

cursor = conection_bd.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        cedula TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        dias_validos INTEGER NOT NULL
    )
''')

def add_customer(name, id, age, valid_days):
    if not name:
        return "El nombre no puede estar vacio."
    if not id:
        return "La cedula no puede estar vacia."
    if not age:
        return "La edad no puede estar vacia."

    try:
        sentence_sql = "INSERT INTO clientes (cedula, nombre, edad, dias_validos) VALUES (?, ?, ?, ?)"
        values = (id, name, age, valid_days)

        cursor.execute(sentence_sql, values)

        conection_bd.commit()

        return f"¡{name} ha sido agregado correctamente!"
    except sqlite3.IntegrityError as e:
        sql = "SELECT 1 FROM clientes WHERE cedula = ? AND nombre = ? AND edad = ?"
        cursor.execute(sql, (id, name, age))

        if cursor.fetchone():
            return f"{name} ya esta en la base de datos"
        else:
            return "La cedula ya esta almacenada en la base de datos pero no coincide con el nombre del cliente."

if not os.path.exists("Clientes_diarios.txt"):
    with open("Clientes_diarios.txt", "x") as file:
        file.write("Clientes diarios: \n")

def discount_days(id):
    cursor.execute("SELECT nombre, dias_validos FROM clientes WHERE cedula = ?", (id,))
    fila = cursor.fetchone()

    if fila:
        name_bd, days = fila

        print("Registro encontrado:")
        print(f"Nombre: {name_bd}")
        print(f"Dias validos: {days}")

        if days > 0:
            confirm_action = input(f"Deseas descontar un dia a {name_bd} (s/n): ").lower().strip()

            with open("Clientes_diarios.txt", "a") as file:
                file.write(f"{name_bd} \n")

            if confirm_action == 's':
                days -= 1
                try:    
                    cursor.execute("UPDATE clientes SET dias_validos = ? WHERE cedula = ?", (days, id))

                    if cursor.rowcount > 0:
                        conection_bd.commit()
                        return f"Se actualizó los dias validos de {name_bd} a {days}."

                except sqlite3.Error as e:
                    return f"Error de base de datos: {e}"
            
            elif confirm_action == 'n':
                return f"No se modificaron los dias de {name_bd}"
        else: 
            return f"{name_bd} ya cumplió con la cantidad de dias."
    else:
        return "No se encontro a nadie con esa cédula."

flag = True

while flag:
    print("Menu principal:")
    print("1. Añadir clientes.")
    print("2. Descontar dias.")
    print("3. Clientes diarios.")
    print("4. Salir.")

    try:
        select_option = int(input("Ingresa el numero de la opcion deseada: "))
    except ValueError:
        print("Debes seleccionar el numero de la opcion.")
        time.sleep(3)
        continue

    match select_option:
        case 1:
            new_client = add_customer(
                name=input("Ingresa el nombre del cliente: ").title().strip(),
                id=input("Ingresa la cédula: ").strip(),
                age=int(input("Ingresa la edad: ")),
                valid_days=int(input("Ingresa la cantidad de dias validos: "))
            )
            print(new_client)
            time.sleep(3)
            os.system('cls')
        case 2:
            update_days = discount_days(
                id=input("Ingresa la cédula: ").strip()
            )
            print(update_days)
            time.sleep(3)
            os.system('cls')
        case 3:
            with open("Clientes_diarios.txt", "r") as file:
                rows = file.readlines()
                for row in rows:
                    print(f"- {row}")
            time.sleep(3)
            os.system('cls')
        case 4:
            option_delete = input("¿Eliminar la lista de clientes diarios? (s): ").lower().strip()
            if option_delete == "s":
                os.remove("Clientes_diarios.txt")
            print("Saliendo del programa...")
            conection_bd.close()
            break
        case _:
            print("Opcion invalida. Selecciona una opcion del menu.")