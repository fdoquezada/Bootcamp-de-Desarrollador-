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
        self._origen='nacional'
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

class Cliente:
    def __init__ (self, idcliente, nombre,apellido,correo,fecha_registro, saldo, antiguedad):        #agrega atributo 'antiguedad'
        self.idcliente = idcliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.antiguedad=antiguedad
        self.saldo=saldo
        self.__impuesto=producto.retornar_iva()

    def retornar_saldo(self):
        self.saldo=self.saldo
        return self.saldo
    
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
        self.__saldo=cliente.retornar_saldo()
        self.__impuesto=producto.retornar_iva()
        self.precio_venta=producto.valor_neto

    def vender(self,cliente_inst,producto_inst,vendedor_inst,proveedor_inst):       #metodo 'vender'
        
        #print(cliente_inst.nombre)
        #print(producto_inst.nombre)
        respuesta_unidades=True                             #validacion de unidades y saldo disponible
        while respuesta_unidades:
            uni_venta=int(input('\ningrese unidades a vender: '))
            if uni_venta>producto_inst.stock:
                print('\nNo hay suficientes unidades en inventario para esta venta')        #mensaje validacion para unidades compradas con stock producto
            else:

                venta_pesos=producto_inst.valor_neto*uni_venta      #calculo de venta
                valor_final=int(venta_pesos*self.__impuesto)
                if valor_final>cliente_inst.retornar_saldo():
                    print('\nUsted no tiene saldo suficiente para efectuar esta venta')   #mensaje validacion para venta con saldo cliente
                else:
                    respuesta_unidades=False
                    iva_total=int(valor_final-venta_pesos)      #calculo del iva
                    print('Unidades vendidas:   ',uni_venta)
                    print('La venta total es $', venta_pesos)
                    print('\nvalor neto:\t', venta_pesos)
                    print('IVA:\t\t', iva_total)
                    print('      \t\t---------')
                    print('valor final:\t',int(valor_final),'\n')
                    
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
                    cliente_inst.saldo=int(cliente_inst.retornar_saldo()-valor_final)
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
        
proveedor1=Proveedor ('9.999.999-3', 'nombrelegal', 'razonsocial','china', 'personajuridica')   #instancia de 1 proveedor
producto=Producto("1","zapatillas","vestuario","Nike",200,25000,1.19)       #instancia 1 producto
producto.imprimir_producto()
producto.precio_en_dolares('pesos')         #llama metodo sobrecarga con 1 parametro
producto.precio_en_dolares('pesos','dolares')  #llama metodo sobrecarga con 2 parametro
cliente=Cliente("0001","vale","sanchez","vale@hotmail.com", '05/07/2021', 150000, "antiguedad")  #instancia cliente
vendedor=Vendedor("21.003.234-2", "Juan", "Alvarez", "vestuario",1000000, 500)      #instancia vendedor
vendedor.vender(cliente,producto,vendedor,proveedor1)       #instancia metodo "vender"
vendedor.impresion_vendedor_comision(cliente,producto,vendedor,proveedor1)  #instancia metodo 'impresion comision vendedor'
vendedor.impresion_cliente_saldo(cliente,producto,vendedor,proveedor1)   #instancia metodo 'impresion saldo clientee'

###check###
print('\n************PRINT PARA CHECK *****************')
print('nuevo saldo', cliente.retornar_saldo())
print('nuevo stock', producto.stock)
print('comision acumulada', vendedor.comision_pesos)
