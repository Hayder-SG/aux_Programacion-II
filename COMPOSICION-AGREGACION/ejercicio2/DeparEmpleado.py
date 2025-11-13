class Departamento:
    def __init__(self, nombre, area):
        self.__nombre = nombre
        self.__area = area
        self.empleados = []
        
    #b) Agregar el metodo mostrarEmpleados()
    def mostrarEmpleados(self):
        print(f"Los empleados del departamento {self.__nombre} son:")
        for empleado in self.empleados:
            empleado.mostrar()
        print("")
    
    #c) Implementar cambioSalario() para todos los empleados de un departamento en específico.
    def cambioSalario(self, salario):
        for empleado in self.empleados:
            empleado.setSueldo(salario)
    
    #d) Verificar si algun empleado del departamento 1 pertenece al departamento 2.
    def verificarDep1(self):
        existe = False
        for empleado in self.empleados:
            if empleado.getDepartamento() == dep2:
                print(f"{empleado.getNombre()} pertenece también al departamento 2")
        if not existe:
            print("Ningún empleado de dep1 pertenece a dep2")

    #e) Mover los empleados del departamento 1 al departamento 2. Tras eso mostrar de nuevo los departamentos.
    def mover_empleados(self, dep):
        for empleado in self.empleados:
            dep.empleados.append(empleado)
        self.empleados = []

class Empleado:
    def __init__(self, nombre, cargo, sueldo, departamento = None):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__sueldo = sueldo
        self.__departamento = departamento
    
    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSueldo(self):
        return self.__sueldo
    
    def getDepartamento(self):
        return self.__departamento

    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Cargo: {self.__cargo}, Sueldo: {self.__sueldo}")

    def setSueldo(self, nSalario):
        if nSalario >= 0:
            self.__sueldo = nSalario
        else:
            print("El salario no puede ser negativo")

#a) Instanciar 2 departamentos, uno con 5 empleados y el otro sin empleados.
dep1 = Departamento("Departamento limpieza", "Area 1")
dep2 = Departamento("Departamento mantenimiento", "Area 2")  

empleado1 = Empleado("Juan 1", "Cargo 1", 1000, dep1)
empleado2 = Empleado("Pepe 2", "Cargo 2", 2000, dep1)
empleado3 = Empleado("Maria 3", "Cargo 1", 3000, dep1)
empleado4 = Empleado("Jose 4", "Cargo 3", 4000, dep1)
empleado5 = Empleado("Alicia 5", "Cargo 2", 5000, dep1)

dep1.empleados = [empleado1, empleado2, empleado3, empleado4, empleado5]

dep1.mostrarEmpleados()
dep2.mostrarEmpleados()

dep1.cambioSalario(1500)

dep1.mostrarEmpleados()
dep2.mostrarEmpleados()

dep1.verificarDep1()

#e) Mover los empleados del departamento 1 al departamento 2. Tras eso mostrar de nuevo los departamentos.
dep1.mover_empleados(dep2)

dep1.mostrarEmpleados()
dep2.mostrarEmpleados()