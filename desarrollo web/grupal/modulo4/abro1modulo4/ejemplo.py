class Agenda():
    def __init__ (self):
        self.contactos = {}

    def cargar_clientes(self):
        idcliente = input ("ingrese su id de clientes: ")
        nombre =input("ingrese el nombre del clientes: ")
        apellido = input ("Ingrese su apellido")
        correo = input ("Ingrese su mail: ")
        fecha_registro = input ("Ingrese su fecha de registro")
        __saldo = input ("saldo")
        self.contactos[idcliente] = (nombre,apellido,correo,fecha_registro,__saldo)
        print("fin de carga de contacto")

    def listar_clientes(self):
        print("listado de clientes")
        for idcliente in self.clientes:
            print(idcliente, self.clientes[idcliente][0],self.clientes[idcliente][1],self.clientes[idcliente][2],self.clientes[idcliente][3],self.clientes[idcliente][4])
            print("fin listado clientes")

    def menu (self):
        option=0
        while option !=3:
            print("menu de agenda")
            print("1.-cargar clientes ")
            print("2.-listar agenda de clientes")
            print("3.-finalizar ")
            option= int(input ("Seleccione la opccion deseada"))
            if option == 1:
                self.cargar_clientes
            elif option == 2:
                self.listar_clientes()

agenda = Agenda()   
agenda.cargar_clientes
