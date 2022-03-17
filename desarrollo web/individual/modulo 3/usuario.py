from string import punctuation

def validador_contrasena (cts):
    if len(cts) < 6 or len (cts) > 12:#formulamos que longuitud que debe tener la contraseña
        print("La caontaseña debe tener entre 6 a 12 caracteres")
    elif not any ([c.isdigit() for c in cts]) :#funcion que nos indica que la contraseña debe contar con un digito 
        print ("La caontaseña debe tener algun digitos")#
    elif not any ([c.islower() for c in cts]) :#funcion que nos indica que la contraseña debe contar con una letra minuscula
        print ("La caontaseña debe contener una minuscular")
    elif not any ([c.isupper() for c in cts]) :# funcion que nos indica que la contraseña debe una letra en mayuscula
        print ("La contraseñala debe contener una mayuscula")
    elif not any ([True if c in punctuation else False for c in  cts]): 
        print ("La contrasela debe contener un caracter ") 
    else:
        print ("se establecio correctamente la contraseña")
        return True
    return False     

intentos = 0
while True:
    contrasena = input("ingrese su contraseña: ")
    intentos += 1

    if validador_contrasena (contrasena):    
        print("La contraseña introducida ha sido {}".format(contrasena))
        break
    elif intentos > 3:
        contrasena = None
        print("No ha sido posible establecer una contraseña")
        break


