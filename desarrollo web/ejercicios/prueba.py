"""● En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.
● Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
● Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
● Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
● Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente
su nombre? ¿Cómo solucionarías este problema?
● Convierte tu string en una lista, en la cual cada elemento es un usuario.
● Imprima en pantalla la cantidad usuarios que tiene tu aplicación.
● Imprima en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar
para realizar esto?"""

#listado de integrantes en string 
integrantes =("PEDRO,SANTIAGO,JUAN,ANDRES,BARTOLOME,JUDAS,MATEO,FELIPE")
#se pasa el string a lista con split
listadointegrantes=integrantes.split(",")#se pasa el string a lista con split
#se crea la divicion de los tres entegrantes en string
seleccion= listadointegrantes[0:3]
print (seleccion)
#creamos el bucle y el cierra de el mismo 
i=0

while i <3:
      #se crea la interafas para consultar al usuario
      login = input("ingrese usuario: ")
      print("ingrese usuario: ")
      if login in seleccion:
            usuario = seleccion.index(login)
            print("hola " + login +)
            continue
      else:
            i +=1
            print("lo lamento estas fuera por demaciados intentos fallifos")
            
      
         
    