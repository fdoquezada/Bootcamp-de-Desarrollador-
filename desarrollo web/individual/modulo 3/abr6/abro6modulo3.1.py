"""Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario.
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir
en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’."""
 
                    
class DatosClientes():
    def __init__(self):
        self.usuarios = {}
    
    def cargar_contactos(self):
        nombre = input('Nombre: ')
        contrasena =input('contrasena: ')
        fechanacimiento= int(input('fechanacimiento: '))
        self.usuarios[nombre] = (contrasena, fechanacimiento)
        print("*"*10,"usuarios ingresado al listado", "*"*10)
     
    def definirfechanacimiento(self):
        while True:
            try:
                fechanacimiento = int(input(" ingrese su edad: "))
                break
            except ValueError:
                print("ingrese solo numeros enteros positivos del 18 al 100")   
        
        
        
        
    def listar_clientes(self):   
        print("*"*25) 
        print("listado de usuarios:")
        print("*"*25) 
        for nombre in self.usuarios:
            print(nombre,self.usuarios[nombre][0],self.usuarios[nombre][1])
        print("fin de listado")
        
    """def listar_agenda(self):
        print("\nlistado completo de clientes")
        for nombre in self.usuarios:
            print(nombre,self.usuarios[nombre][0],self.usuarios[1])
            print("*"*25,"adios", "*"*25)"""
                
    def menu (self):
        option=0
        while option !=3:
            print("\n    menu de Opciones")
            print("*"*25,)
            print("1.insertar usuario")
            print("2.lista de usuarios")
            print("3.salir")
            option = int(input("ingresa opcion solicitada: "))
            if option == 1:
                self.cargar_contactos()
            elif option == 2:
                self.listar_clientes()
            elif option == 3:    
                 print("*"*25,"adios gracias por su visita","*"*25)
    lista= [1,2,3]
def mostrar_lista(lista):
    if len(lista) !=0:
        time.sleep(3)     
                    
               
agenda = DatosClientes()
agenda.menu()                                

                



    