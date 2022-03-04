stock = {"ZAPATILLAS": 20, "POLERAS": 10, "ZAPATOS": 15 , "POLERÓN": 3, "CHAQUETA": 5 , "GUANTES": 4 }
clientes = ["Anibal", "Maria", "Francisca", "Pedro", "Ana"]
def usuarios_registrados():
    for nombre in range (0,len(clientes)):
        print(clientes[nombre])

usuarios_registrados()

def compra():
    compra_lista_almacena=[]
    compra_cliente=input('ingrese cliente ')
    while compra_cliente not in clientes:
        compra_cliente=input('Debe ingresar un cliente de la lista de clientes ')
    if compra_cliente in clientes:
            compra_producto=''
            compra_cant='1'
            compra_producto=(input('ingrese producto a comprar ')).upper()
            while compra_producto not in stock.keys():
                compra_producto=input('Debe ingresar un producto de la lista de productos ')
            if compra_producto in stock.keys():
                compra_cant=int(input('ingrese cantidad de producto a comprar ej: 10 '))
    compra_lista_almacena.append(compra_cliente)
    compra_lista_almacena.append(compra_producto)
    compra_lista_almacena.append(compra_cant)
    remanente=stock[compra_producto]-compra_cant
    return remanente            #alamcena valor para seer usado en las funciones siguientes

def validacion_compra():        #Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
    res_validacion=compra()>0
    print(res_validacion)
    return res_validacion

def compra_aprobada():  #Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega virtual(aprueba/cancela)
    if validacion_compra()==True:
        print('compra aprobada y en camino')
    if validacion_compra()==False:
        print('compra cancelada')
compra_aprobada()

