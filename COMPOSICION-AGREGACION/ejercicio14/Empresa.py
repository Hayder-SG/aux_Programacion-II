class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def mostrar_info(self):
        print("===============================")
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Salario: {self.salario}")
        print("===============================")
    
    
                

class Empresa:
    def __init__(self, nombre, empleados):
        self.nombre = nombre
        self.empleados = empleados
    
    def mostrar_info(self):
        print(f"Empresa: {self.nombre}")
        for empleado in self.empleados:
            empleado.mostrar_info()
    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                print("===============================")
                print(f"Empleado encontrado: {empleado.nombre}")
                print(f"Puesto: {empleado.puesto}")
                print(f"Salario: {empleado.salario}")
                print("===============================")
                return empleado
        print("Empleado no encontrado")
        return None
    
    def eliminar_empleado(self, nombre):
        empleado_encontrado = self.buscar_empleado(nombre)
        if empleado_encontrado:
            self.empleados.remove(empleado_encontrado)
            print("Empleado eliminado")
        else:
            print("Empleado no encontrado")
    
    def promedio_salario(self):
        total_salario = 0
        print("Promedio de salario:")
        for empleado in self.empleados:
            total_salario += empleado.salario
        print(total_salario / len(self.empleados))
        print("===============================")
    
    def salario_mayor_a_X(self, X):
        print("Empleados con salario mayor a X:")
        for empleado in self.empleados:
            if empleado.salario > X:
                print(empleado.nombre)
        print("===============================")

e1 = Empleado("Remy", "Chef", 2000)
e2 = Empleado("Alfredo", "Mesero", 1500)
e3 = Empleado("Linguini", "Mesero", 1500)
e4 = Empleado("Colette", "Administrativo", 1800)
e5 = Empleado("Django", "Administrativo", 1800)

empleados = [e1, e2, e3, e4, e5]

empresa = Empresa("Restaurante", empleados)

empresa.mostrar_info()

empresa.buscar_empleado("Linguini")

empresa.eliminar_empleado("Linguini")

empresa.promedio_salario()

empresa.salario_mayor_a_X(1800)