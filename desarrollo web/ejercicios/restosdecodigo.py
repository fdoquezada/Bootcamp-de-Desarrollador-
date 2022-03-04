edad =int(input("ingrese su edad:"))
if ( edad > 29 or edad < 18):
   print("edad no coincide con el rango")
elif (edad >= 25):  
    print("puede pasar")
else:
    print ("lo sirnto no corresponde ")    
    
    
    
    def es_numerico(cadena):#validador si es numero ingredado es valido 
         try:
         int(cadena)
         return True
     except ValueError:
         return False   
if es_numerico(edad):
    print("ha digitado una edad valida")
else:
    print("el  valor digitado no corresponde a numero vuelva")  
    
    
    print("Total Regueton Materiales: "+str(origen))
print("Total Rock: "+str(edad))
print("Total Electronica: "+str(afinidad))

else:
    print ("lo sirnto no corresponde ")    
    
    else:
        print("esta no es una opcion del cuestionarion intentelo nuevamente")
        
        
        
        
        
        
        while True:
        try:
        edad = int(input("ingrese su edad:"))
        break
    except ValueError:
        print("ingrese solo numero enteros positivos")
  