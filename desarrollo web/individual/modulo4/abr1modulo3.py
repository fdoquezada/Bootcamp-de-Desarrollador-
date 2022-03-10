#DESARROLLO
#Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender las
#ventajas de la programación orientada a objetos.
#En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita actualizar lo
#1.-siguiente:Identifica tres tipos de usuarios de su aplicación.
#2.-Identifica tres atributos por tipo de usuario.
#3.-Identifica tres tipos de0Identifica tres acciones que pueden desarrollar cada tipo de usuario. Las acciones se deben ejecutar de
#forma interna en nuestra aplicación. Por ejemplo, acceder a datos sensibles, registrar nuevos usuarios,
#enviar solicitudes de información adicional.
#● Piense en nuevos atributos y acciones que pueden realizar los objetos.
#Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
#gráfica. Desarrollen el ejercicio de forma intuitiva
class Cliente:
    def __init__(self, nombre, apellido, password, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.edad = edad
    
    #def SaberEdad(self):
     #   if self.edad<18:
      #      print("eres mayor de edad")
       # else:
        #    print("eres menor de dad")    
        
        




cliente_1 = Cliente( 'juan', 'quinteros', '1245', '25')
cliente_2 = Cliente('pedro', 'rojas', '1254', '35')
cliente_3 = Cliente('juan', 'quinteros', '1245', '25')        
   
cliente_1 = Cliente()
#cliente_1.SaberEdad 
   
       
        
"""def menu (self):
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
agenda.menu"""