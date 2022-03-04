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
        