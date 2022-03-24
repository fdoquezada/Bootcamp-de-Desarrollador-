

# El atributo stock de la clase producto, pasará de ser un valor a una Composición de la clase Sucursal y esta contará con un límite de stock de 500 productos, lo cual si se agrega o sobrepasa ese límite (de 500) este deberá emitir un mensaje de despacho del producto y sumarlo directamente en el atributo Stock de la clase BodegaPrincipal.

# Pensando en su tienda virtual, identifique casos en los que la técnica del polimorfismo solucionaría problemas de herencia de métodos y atributos.. Definan la utilidad de MRO para determinados ejercicios de herencia.

################ Creados en ABPro4 ######################

class BodegaPrincipal:
    def __init__(self, direccion, Mts2, stock_Bodega): #Clase Padre
        self.direccion = direccion
        self.Mts2 = Mts2
        self.stock_Bodega = stock_Bodega
    
    def despachar_producto_B(self, valor_a_enviar, sucursal_inst): #Debe descontar un valor desde su stock y sumarlo a stock de sucursal
        if (bodega1.stock_Bodega - valor_a_enviar) < 0:
            print("No hay stock suficiente en BODEGA para enviar a sucursal")
        else:
            bodega1.stock_Bodega = bodega1.stock_Bodega - valor_a_enviar  #disminuye stock de Bodega   
            sucursal_inst.recepcionar_producto_S(valor_a_enviar)    #envia stock a Sucursal
            stock_sucursal_actualizado_recepcion=sucursal1.stock_sucursal #llama stock a Sucursal y se lo asigna a una variable
            if stock_sucursal_actualizado_recepcion>500:        #hace la comparacion
                print('no se puede enviar a sucursal porq quedaria mas de 500  en sucursal')
                #si el stock de sucursal (llamado en la linea 21)   es mayor a 500 unidades, revierte las operaciones anteriores
                bodega1.stock_Bodega = bodega1.stock_Bodega + valor_a_enviar     #devuelve stock restado a Bodega
                sucursal_inst.recepcionar_producto_S((-1*valor_a_enviar))   #el envio de stock a sucursal se multiplica por (-1) paraa volverlo negativo para asi descontarlo en el metodo recepcionar_producto_S
    
    def recepcionar_producto_B(self, valor_a_recibir, sucursal_inst): #Sumará valor al stock
        bodega1.stock_Bodega = bodega1.stock_Bodega + valor_a_recibir #suma a bodega unidades enviadas desde sucursal
        sucursal_inst.despachar_producto_S(valor_a_recibir)     #envia ese valor a sucursal para restar de su inventario
        stock_sucursal_actualizado_envio=sucursal1.stock_sucursal #se llama al stock de la sucursal (instanciado)
        if stock_sucursal_actualizado_envio<0:                     # revisa que es stock de la sucursal llamado no sea negativo
            print('no hay stock en SUCURSAL paraa efectuar la operacion')
            #si el stock en la sucursal queda negativo, revierte las operaciones anteriores
            bodega1.stock_Bodega = bodega1.stock_Bodega - valor_a_recibir  #en Bodega, resta el stock sumado anteriormente
            sucursal_inst.despachar_producto_S((-1*valor_a_recibir))    #se devuelve el valor para sumarlo a sucursal
    
class Sucursal(BodegaPrincipal): #Clase hija
    def __init__(self, direccion, Mts2, stock_Bodega, stock_sucursal):
    
        BodegaPrincipal.__init__(self, direccion, Mts2, stock_Bodega)
        self.stock_sucursal = stock_sucursal
        
    def despachar_producto_S(self, valor_a_recibir):#Deberá descontar stock de la sucursal y agregarlo al stock de la clase BodegaPrincipal
        self.stock_sucursal = self.stock_sucursal - valor_a_recibir     ###operacion desde la Sucursal (envia a bodega principal)
        if self.stock_sucursal<50:
            print('stock bajo 50, necesita pedir 300 unidades a bodega')
            valor_a_enviar=int(300)
            super().despachar_producto_B(valor_a_enviar, sucursal1)


    def recepcionar_producto_S(self, valor_a_enviar):
        self.stock_sucursal = self.stock_sucursal + valor_a_enviar  ###operacion desde la Sucursal (recibe desde bodega principal)
        if self.stock_sucursal<50:
            print('stock bajo 50, necesita pedir 300 unidades a bodega')
            valor_a_enviar=int(300)
            super().despachar_producto_B(valor_a_enviar, sucursal1)

            
        
"""
Si el atributo stock de la clase Sucursal cuenta con un stock menos de 50, este automáticamente deberá
mostrar un mensaje el cual indique que se está solicitando y reponiendo productos y desde la clase Bodega
se deberá descontar 300 del atributo stock y sumarlos a Sucursal. En el caso de que no quede suficiente
stock en la clase Bodega, deberá indicar a través de un mensaje que no existe stock suficiente para reponer.
Se debe implementar la función super() para poder acceder a los atributos y métodos de clases superiores.
Se deberá implementar una clase OrdenCompra con los siguientes atributos:

a. Id_ordencompra
b. producto
c. despacho
El atributo producto, deberá ser una composición de la clase Producto y el atributo despacho, solo
almacenará valores booleanos. En el caso de que el despacho sea True ( Verdadero ), se deberá agregar al
valor del producto 5.000 CLP por recargo de despacho y mostrar por consola el total final con el detalle (
valor neto, impuesto, despacho, valor total ) el valor final del producto, cuando se utilice la función vender
de la clase Vendedor.

"""
######  ABPro 5 ######

############# Traído del ABPro2 #########################

class Proveedor:            #creacion clase Proveedor
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_personalidad): #definicion init
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_personalidad=tipo_personalidad

class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock,valor_neto,__impuesto):     #se agrega atributo origen
        self.sku = sku
        self.nombre = nombre        
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto=valor_neto
        self.__impuesto=1.19
        self.origen='nacional'
        self.nombre_proveedor=proveedor1.nombre_legal

    def retornar_iva(self):
        iva_impuesto=producto.__impuesto
        return iva_impuesto

    def mostrar_productos(self):    #mostrar producto por pantalla
        print(self.sku, self.nombre, self.categoria, self.proveedor,self.stock, self.valor_neto)
    
    def imprimir_producto(self):    #impresion producto 
        print('\nProducto elegido:  ', self.nombre) 
        print('Categoria: ', self. categoria)
        print('Proveedor:   ',self.nombre_proveedor)        #composicion de producto/proveedor en instanciamiento
        print('Stock actual es:   ',self.stock)
        print('Valor neto por unidad:   $', self.valor_neto)

        
    def precio_en_dolares(self, pesos=None, dolares=None):      # metodo sobrecarga
        if pesos is not None and dolares is None:
            print('\nEl valor unitario es', self.valor_neto,'pesos')
        elif pesos is not None and dolares is not None:
            print('El valor unitario es',self.valor_neto ,'pesos igual a ',self.valor_neto/800,'dolares')

class OrdenCompra:
    def __init__(self,id_ordencompra, despacho):
        self.id_ordencompra = id_ordencompra
        self.sku = producto.sku
        self.nombre = producto.nombre        
        self.categoria = producto.categoria
        self.proveedor = producto.proveedor
        self.stock = producto.stock
        self.valor_neto=producto.valor_neto
        self.__impuesto=1.19
        self.despacho = despacho

    def quiere_despacho(self):
        despachar_orden=input('Quiere despachar la orden? (s/n)')
        if despachar_orden=='s':
            self.despacho=True
        else: 
            despachar_orden=='n'
            self.despacho=False
        return self.despacho

class Cliente:
    def __init__ (self, idcliente, nombre,apellido,correo,fecha_registro, saldo, antiguedad):        #agrega atributo 'antiguedad'
        self.idcliente = idcliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.antiguedad=antiguedad
        self.__saldo=saldo
        self.__impuesto=producto.retornar_iva()

    def retornar_saldo(self):
        return self.__saldo
    
    def modificar_saldo(self, venta_final):
        self.__saldo=self.__saldo - venta_final

    def impresion_cliente(self):    #imprime saludo y saldo actual
        print('\nBuenos dias ', self.nombre, self.apellido,'. Su saldo actual es: $ ',self.saldo, '\n')

class Vendedor:
    def __init__(self, run, nombre, apellido, seccion,metas_venta,comision_pesos):       #agrega atributo 'metas de venta'
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0.5
        self.comision_pesos=500
        self.metas_venta=metas_venta
        self.stock=producto.stock
        self.saldo=cliente.retornar_saldo()
        self.__impuesto=producto.retornar_iva()
        self.precio_venta=producto.valor_neto
        self.despacho=orden_compra1.quiere_despacho()

    def vender(self,cliente_inst,producto_inst,vendedor_inst,proveedor_inst,orden_compra_inst):       #metodo 'vender'
        
        #print(cliente_inst.nombre)
        #print(producto_inst.nombre)
        respuesta_unidades=True                             #validacion de unidades y saldo disponible
        while respuesta_unidades:
            uni_venta=int(input('\ningrese unidades a vender: '))
            if uni_venta>producto_inst.stock:
                print('\nNo hay suficientes unidades en inventario para esta venta')        #mensaje validacion para unidades compradas con stock producto
            else:
                venta_pesos=producto_inst.valor_neto*uni_venta      #calculo de venta
                iva_total=int(venta_pesos*(self.__impuesto-1))
                if self.despacho==True:
                    valor_despacho=5000
                else:
                    valor_despacho=0
                valor_final=venta_pesos+iva_total+valor_despacho
                if valor_final>cliente_inst.retornar_saldo():
                    print('\nUsted no tiene saldo suficiente para efectuar esta venta')   #mensaje validacion para venta con saldo cliente
                else:
                    respuesta_unidades=False

                    #calculo del iva
                    print('\nOrden Compra# ', orden_compra1.id_ordencompra,'\n')     #resumen de venta incluye / no incluye valor despacho
                    print('\nUnidades vendidas:   ',uni_venta)
                    print('La venta total es $', venta_pesos)
                    print('\nvalor neto:\t$', venta_pesos)
                    print('IVA:\t\t$', iva_total)
                    print('\ndespacho:\t$', valor_despacho )
                    print('      \t\t---------')
                    print('\nvalor final:\t$',int(valor_final),'\n')
                    
          
                    ##stock##
                    #print('\nProducto: ',prod_venta)
                    print('\nEl stock inicial es ', producto_inst.stock)    # calculo para descontar stock
                    print('Se vendieron ' ,uni_venta)
                    producto_inst.stock=producto_inst.stock-uni_venta
                    print('Stock despues de la venta: ',producto_inst.stock,'\n')
                    
                    ##comision##
                    comision_pesos_calculada=int(venta_pesos*self.__comision/100)   #calculo comision en base a % data en init
                    #print('\nVendedor: ',self.nombre, self.apellido)
                    print('\nLa comision inicial es ', vendedor_inst.comision_pesos)
                    vendedor_inst.comision_pesos=vendedor_inst.comision_pesos+comision_pesos_calculada
                    print('La comision obtenida por la venta es ', comision_pesos_calculada)
                    print('La comision acumulada es ', vendedor_inst.comision_pesos)

                    ##descuento saldo##
                    #print('\nCliente: ', cliente_venta)
                    print('\nEl saldo inicial es: ',cliente_inst.retornar_saldo())      #descuenta venta a saldo inicial
                    print('El gasto en su compra: ',valor_final)
                    cliente_inst.modificar_saldo(valor_final)
                    print('El nuevo saldo es ', cliente_inst.retornar_saldo())
                    
                    ###agrega stock por proveedor
                    uni_prov=int(input('Ingresar unidades que entrega proveedor: '))    #agrega unidades al stock (por proveedor)
                    producto_inst.stock=producto_inst.stock+ uni_prov
                    print('nuevo stock que (-venta) (+prov): ', producto_inst.stock)
                    
                    return self.stock

    def impresion_vendedor_comision(self,cliente_inst,producto_inst,vendedor_inst,proveedor_inst):      #imprime comision acumulada para 1 vendedor
        print('\n',vendedor_inst.nombre, 'tiene una comision acumulada de ' ,vendedor_inst.comision_pesos)
        
    def impresion_cliente_saldo(self,cliente_inst,producto_inst,vendedor_inst,proveedor_inst):      #imprime saldo para 1 cliente
        print('\n',cliente_inst.nombre, 'tiene un saldo acumulado de ' ,cliente_inst.retornar_saldo())

########### Instanciación ABPro2 ######################

proveedor1=Proveedor ('9.999.999-3', 'nombrelegal', 'razonsocial','china', 'personajuridica')   #instancia de 1 proveedor
producto=Producto("1","zapatillas","vestuario","Nike",55,5000,1.19)       #instancia 1 producto = producto inicial
producto.imprimir_producto()
producto.precio_en_dolares('pesos')         #llama metodo sobrecarga con 1 parametro
producto.precio_en_dolares('pesos','dolares')  #llama metodo sobrecarga con 2 parametro
orden_compra1=OrdenCompra('00002', True)
#orden_compra1.quiere_despacho()

cliente=Cliente("0001","vale","sanchez","vale@hotmail.com", '05/07/2021', 1500000, "antiguedad")  #instancia cliente
vendedor=Vendedor("21.003.234-2", "Juan", "Alvarez", "vestuario",1000000, 500)      #instancia vendedor
vendedor.vender(cliente,producto,vendedor,proveedor1,orden_compra1)       #instancia metodo "vender"
vendedor.impresion_vendedor_comision(cliente,producto,vendedor,proveedor1)  #instancia metodo 'impresion comision vendedor'
vendedor.impresion_cliente_saldo(cliente,producto,vendedor,proveedor1)   #instancia metodo 'impresion saldo clientee'

###check###
print('\n************PRINT PARA CHECK *****************')
print('nuevo saldo', cliente.retornar_saldo())
print('nuevo stock', producto.stock)
print('comision acumulada', vendedor.comision_pesos)

################ Instanciación ABPro4 ################        
valor_a_enviar = int(input("Ingrese el valor a mover de Bodega a Sucursal: "))
bodega1 = BodegaPrincipal("Valparaíso", "50", 305)
sucursal1 = Sucursal("Santiago", "30", 305, producto.stock )
bodega1.despachar_producto_B(valor_a_enviar, sucursal1)

print("El stock actualizado en la sucursal es: ",sucursal1.stock_sucursal)
print("El stock actualizado en Bodega es: ",bodega1.stock_Bodega)

valor_a_recibir = int(input("Ingrese el valor a mover de Sucursal a Bodega: "))
bodega1.recepcionar_producto_B(valor_a_recibir, sucursal1)

print("El stock actualizado en la sucursal es: ",sucursal1.stock_sucursal)
print("El stock actualizado en Bodega es: ",bodega1.stock_Bodega)

