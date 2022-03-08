#Creación de las clases
class clientes:
    def __init__ (self, idcliente,nombre,apellido,correo,fecha_registro, saldo):
        self.idcliente = idcliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo

    
    def imprimir_nombres(self):
        print(self.nombre, self.apellido, self.correo)
    
    def agregar_saldo(self):
        nombre = input("ingrese su nombre:")
        saldo = int(input("Ingrese saldo:"))
        print("se agrega", saldo, "al cliente",nombre)

    """def agregar_saldo_cliente(self, clasificacion):
        saldo = 20000
        if clasificacion == "buena":
            print("se agregan", saldo, "de saldo a cliente")
        else:
            print("mo se puede agregar saldo a cliente")
    
    def mostrar_saldo_cliente(self):
        saldo = 20000
        print("el saldo del cliente son", saldo)"""
    

#usuarios = clientes("hola","maria","carreño","maria@hotmail.com","03/04/2022","20000")

#usuarios.imprimir_nombres()
cliente1 = clientes("hola","maria","carreño","maria@hotmail.com","03/04/2022","20000")
#cliente1.mostrar_saldo_cliente()
#cliente1.agregar_saldo_cliente("buena")
cliente1.agregar_saldo()

class productos:
    def __init__(self, sku,nombre,categoria,proveedor,stock, valor_neto,__impuesto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self._impuesto = 1.19
    
    def ingresar_producto(self):
        sku = input("ingrese sku del producto")
        nombre = input("ingrese un producto:")
        categoria = input("ingrese la categoria a la que pertenece el producto:")
        proveedor = input("ingres proveedor del producto:")
        stock = int(input("Ingrese stock:"))
        valor_neto = int(input("ingrese valor neto del producto:"))
        valor_total = (valor_neto * self._impuesto)
        print("el producto", nombre, "con sku:", sku, "se agregado a la categoria", categoria, "del proveedor", proveedor,"con un stock", stock, "con un valor neto de", valor_neto, "a un impuesto de", self._impuesto, "que da un total de", valor_total)

producto1 = productos("1","2","3","4","5","6","7")
print(producto1)
producto1.ingresar_producto()

class vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        

#cliente1 = clientes()