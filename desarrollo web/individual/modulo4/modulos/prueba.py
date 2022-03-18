class Agenda():
    def __init__(self):
        self.contactos = {}
    
    def cargar_contactos(self):
        nombre = input('Nombre: ')
        telefono =input('Telefono: ')
         = input('Mail: ')
        self.contactos[nombre] = (telefono, mail)
        print("*"*25,"fin de programa", "*"*25)
        
    def listar_clientes(self):    
        print("listado de clientes")
        for nombre in self.contactos:
            print(nombre,self.contactos[nombre][0],self.contactos[nombre][1])
        print("fin de listado")
        
    def listar_agenda(self):
        print("listado complero de agenda")
        for nombre in self.contactos:
            print(nombre,self.contactos[nombre][0],self.contactos[1])
        print("fin del programa") 
                
    def menu (self):
        option=0
        while option !=3:
            print("menu de Opciones")
            print("1.insertar clinete")
            print("2.insertar clinete")
            print("3.salir")
            option = int(input("ingresa opcion solicitada: "))
            if option == 1:
                self.cargar_contactos()
            elif option == 2:
                self.listar_clientes()    
                
agenda = Agenda()
agenda.menu()                                

                



    