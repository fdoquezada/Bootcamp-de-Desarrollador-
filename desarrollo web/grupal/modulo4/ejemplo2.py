class Productos:
    def __init__(self, sku,nombre,categoria,proveedor,stock, valor_neto,):
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

    def menu (self):
            option=0
            while option !=3:
                print("menu de agenda")
                print("1.-cargar clientes ")
                print("2.-listar agenda de clientes")
                print("3.-finalizar ")
                option= int(input ("Seleccione la opccion deseada"))
            if option == 1:
                self.ingresar_producto
            elif option == 2:
                self.listar_clientes()


producto1 = Productos("1","2","3","4","5","6","7")

agenda = Productos()
agenda.menu