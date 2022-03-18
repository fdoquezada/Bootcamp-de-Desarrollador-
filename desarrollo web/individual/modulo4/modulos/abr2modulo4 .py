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
from multiprocessing.connection import Client


print("*"*25,"usuarios a presentar","*"*25)
class Cliente:
    contador = 0
    def __init__(self, nombre, apellido, password, edad):
        Cliente.contador +=1
        self.cliente = Cliente.contador
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.edad = edad

        
    def __str__ (self):
        return str (self.cliente) + " " + self.nombre + " " + self.apellido + " " + self.password + " " + self.edad
    
    def impresion_cliente(self):   
        print('\nBuenos dias ', self.nombre, self.apellido,' Su edad actual es:  ',self.edad, '\n')  
    
    def presentacion(self):
        print("hola soy " + self.nombre + " y tengo " + self.edad + " años de edad" )

 
 
usuario1 = Cliente("Fernando","Quezada","12345","35" )
usuario2 = Cliente("juan","Lopez","854545","35" )
usuario3 = Cliente("Andres","Ordones","12345","35" )
usuario4 = Cliente( 'juan', 'quinteros', '1245', '25')
usuario5 = Cliente('pedro', 'rojas', '1254', '35')
usuario6 = Cliente('juan', 'quinteros', '1245', '25')

usuario1.impresion_cliente()
usuario2.impresion_cliente()
usuario1.presentacion()

print(usuario1)    
print(usuario2)
print(usuario1.__dict__)
usuario7= Cliente('Pedro', 'Lopez', '12156', '25')
print(usuario7)










     
   
