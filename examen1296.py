class cliente1296:
    
    id_cliente = 0
    no_telefono = ""
    correo = ""
    edad = 0
    curp = "" 
    RFC = ""
    sexo = ""

    # Función para mostrar los datos del cliente
    def mostrar_datos1296(self):
        print(f"ID_CLiente: {self.id_cliente}")
        print(f"Numero de telefono: {self.no_telefono}")
        print(f"Correo: {self.correo}")
        print(f"Edad: {self.edad}")
        print(f"Curp: {self.curp}")
        print(f"RFC: {self.RFC}")
        print(f"Sexo: {self.sexo}")

    # Funcion para listar 7 clientes (lista)
    def Listar_clientes1296(self):
        clientes = [
            {"Cliente 1": "Nika"},
            {"Cliente 2": "Valentina"},
            {"Cliente 3": "Ever"},
            {"Cliente 4": "Alexis"},
            {"Cliente 5": "Renata"},
            {"Cliente 6": "Ailin"},
            {"Cliente 7": "Alex"}
        ]
        for cliente in clientes:
            print(cliente)

    # Función para listar 7 correos (tupla)
    def Tupla_correo1296(self):
        correos = ("nik4@gmail.com", "valeco@gmail.com", "Ev3r@gmail.com", "alexicom@gmail.com", "renaca@gmail.com", "ailinn@gmail.com", "al3x@gmail.com")
        print("Correos:")
        for correo in correos:
            print(correo)

    # Función para crear su edad + sexo
    def Dicionario_sexo_edad1296(self):
        dicionario = {
            "Femenino": 19,
            "Femenino": 22,
            "Masculino": 18,
            "Masculino": 24,
            "Femenino": 24,
            "Femenino": 22,
            "Femenino": 19
        }
        print("Sexo y edad:")
        for sexo, edad in dicionario.items():
            print(f"{sexo}: {edad}")

    # Función para dar de alta a un alumno
    def alta(self):
        print("La operación de alta se realizó correctamente para los datos del cliente.")

    # Función para dar de baja a un alumno
    def baja(self):
        print("La operación de baja se realizó correctamente para los datos del cliente.")

# Crear el objeto de la clase
obj = cliente1296()

# Asignar datos a los atributos
obj.id_cliente = 3
obj.no_telefono = "656 100 1221"
obj.correo = "dieg0@gmail.com"
obj.edad = 17
obj.curp = "R0CD12D25JRCH07"
obj.RFC = "1234"
obj.sexo = "Masculino"

# Utilizar los objetos y llamar a las funciones
# Mostrar datos 
obj.mostrar_datos1296()
obj.Listar_clientes1296()
obj.Tupla_correo1296()
obj.Dicionario_sexo_edad1296()
obj.alta()
obj.baja()
