"""Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario.
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir
en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’."""
#def ingreso_usuarios():
menuprincipal = int(input("menu principal: \n 1-Agregar cliente: \n 2-Agregar contraseña: \n 3-reiengrese contraseña: \n 0-salir \n "))
while menuprincipal != 0:
    
    if menuprincipal == 1:
        print ("ingrese nombre cliente")
    elif menuprincipal == 2:
        print ("ingrese contraseña ")
    elif menuprincipal == 3:
        print ("ingrese fecha de nacimiento")
    else:
        print ("favor ingrese una opccion corresta")   
    menuprincipal = int(input("menu principal: \n 1-Agregar cliente  \n 2-Agregar contraseña  \n 3-reiengrese contraseña \n 0-salir \n"))         







usuario = input("Ingrese el usuario: ")
caracteres = len(usuario)
tipo = usuario.isalnum()
if tipo == True:
    if caracteres < 6:
        print("Se debe ingresar por lo menos 6 caracteres ")
    elif  caracteres > 12:
       print ("debe contener menoos de 12 caracteres")     
    else: 
        print("bienbenidos")
else: 
      print("error, valor incorrecto")  
        
        
def lee_entero():
       while True:
       entrada = raw_input("Escribe un numero entero: ")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print "La entrada es incorrecta: escribe un numero entero"""    
           
           
variable = "ferna"
var2 = 1000

match = variable
case "ferna" : print ("hola", variable)
case  "patrcia" : print ("que tal", variable) 
case  "andres" : print ("que tal como vas", variable)
case _: print ("error")
                 