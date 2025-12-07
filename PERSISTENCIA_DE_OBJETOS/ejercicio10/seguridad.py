import json
import hashlib
import os


# -----------------------------
# Clase Usuario
# -----------------------------
class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = self.cifrar(contrasena)

    def cifrar(self, contrasena):
        return contrasena
    #    return hashlib.sha256(contrasena.encode()).hexdigest() #cifrado de contraseña 

    def to_dict(self):
        return {
            "nombre": self.nombre_usuario,
            "contrasena": self.contrasena
        }


# -----------------------------
# Clase GestorUsuarios
# -----------------------------
class GestorUsuarios:
    ARCHIVO = "usuarios_seguro.json"

    def __init__(self):
        # Si no existe el archivo, crearlo con una lista vacía
        if not os.path.exists(self.ARCHIVO):
            with open(self.ARCHIVO, "w") as f:
                json.dump([], f)

    def cargar_datos(self):
        with open(self.ARCHIVO, "r") as f:
            return json.load(f)

    def guardar_datos(self, datos):
        with open(self.ARCHIVO, "w") as f:
            json.dump(datos, f, indent=4)

    def agregar_usuario(self, usuario):
        datos = self.cargar_datos()
        datos.append(usuario.to_dict())
        self.guardar_datos(datos)
        print("Usuario guardado correctamente.\n")

    def mostrar_usuarios(self):
        datos = self.cargar_datos()
        if not datos:
            print("No hay usuarios registrados.\n")
            return

        print("\n--- LISTA DE USUARIOS ---")
        for u in datos:
            print(f"Usuario: {u['nombre']} | Contraseña: {u['contrasena']}")
        print()

    def buscar_usuario(self, nombre):
        datos = self.cargar_datos()
        for u in datos:
            if u["nombre"] == nombre:
                print("\nUsuario encontrado:")
                print(f"Usuario: {u['nombre']}")
                print(f"Contraseña cifrada: {u['contrasena']}\n")
                return
        print("No se encontró el usuario.\n")


# ------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------
def menu():
    gestor = GestorUsuarios()

    while True:
        print("=== SISTEMA DE USUARIOS SEGUROS ===")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            usuario = Usuario(nombre, contrasena)
            gestor.agregar_usuario(usuario)

        elif opcion == "2":
            gestor.mostrar_usuarios()

        elif opcion == "3":
            nombre = input("Ingrese nombre a buscar: ")
            gestor.buscar_usuario(nombre)

        elif opcion == "4":
            print("Saliendo... gracias!")
            break

        else:
            print("Opción inválida.\n")

menu()
