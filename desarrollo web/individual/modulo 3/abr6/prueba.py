from threading import activeCount


class clientes:
    def __init__(self, nombre, apellido ):           
        self.nombre = nombre
        self.apellido = apellido
        self.credito = False
        self.actividad = False
        
    def distribucion(self):
        self.credito= True
    def activo(self):
        self.actividad= True
    def estado(self):
        print("nombre: ", self.nombre, "\napellido: ", self.apellido, "\ncredito: ", self.credito, "\nactividad: ", self.actividad)

class estadocliente(clientes):
        def estado(self,client):
            self.clints = client
            if(self.client):
                return "cliente activo en el sistema de estad"
        
    
        
class cliente(clientes):
    lista =""
    def listado(self):
     self.lista="se encuentra en la lista del proveedor"   
    
    def estado(self):
        print("nombre: ", self.nombre, "\napellido: ", self.apellido, "\ncredito: ", self.credito, "\nactividad: ", self.actividad, "\nlista_cliente: ",self.lista)
        
             
        

pro=cliente("fernando","quezada")

pro.estado()