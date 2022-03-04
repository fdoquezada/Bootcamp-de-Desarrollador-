"""Guarde la información de los productos en una bodega virtual.
● Los productos son vasos, cucharas, cuchillos y tenedores. Cada producto debe tener un stock
aleatorio entre 300 y 500 unidades y una descripción del producto.
● Debe definir funciones que puedan:
● Sumar y disminuir el número de unidades por producto.
● Agregar nuevos productos.
● Quitar productos de la bodega virtual.
● Mostrar todos los productos disponibles y su stock. Debe tener un desfase de un segundo entre
cada producto.
● Verificar si un producto tiene menos de 400 unid"""
import random 
#bodega
bodega = ["vasos","a","esto es un vaso", "cucharas","a","estas son cucharas","cuchillos", "a", "estos son cuchillos","tenedores ","a", "estos son tenedres"]
def stock_aletorio():
        #forstock in[bodega.values():
            #for keys,values in bodega.items():
                #v = random.sample(range(300, 500), 1)
                #v = random.sample(range(300, 500), 1)
            #stock.insert(0,v) #for valores,desc in stock:
               # valores = inventario
                stock_random=random.sample(range(300,400), 4)
                print(stock_random)
   

            
                #print(v)
   
           #print(stock[0])
           
        #for i in stock:
         
        #for i in range(0,len(bodega.values)) 
        #print(bodega)  

stock_aletorio()
            
#clientes

#envios