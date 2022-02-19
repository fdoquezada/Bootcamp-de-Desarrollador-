string_usuarios =("PATRICIA,ELIZABETH,MARCELA,MONSERRAT,VICTOR,JORGE,KARINA")
lista_usuarios=string_usuarios.split(',')
lista_seleccion= lista_usuarios[0:3]
print(lista_seleccion)
print("La cantidad de usuarios registrados es: " + str(len(lista_usuarios)))
i = 0  # contador de intentos fallidos

while i < 3:
    usuario = input("Buscar usuario: ")
    usuario = usuario.upper()
    print(usuario)
    if usuario in lista_seleccion:
        integrante = lista_seleccion.index(usuario)
        print("¡Hola " + usuario + "!, que tengas un muy buen dia")
        continue
    else:
        i += 1
        print("Buen día, No estás Seleccionado o Aun no estás registrado")
    continue
else:
    print("Se ha excedido el número de intentos")