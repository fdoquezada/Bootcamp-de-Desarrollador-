"""● Para desarrollar de mejor forma tu aplicación, requieres conocer mejor a los usuarios que la
utilizarán. Antes de continuar desarrollando, debes elaborar un programa que tiene la funcionalidad de
enviar cuestionarios a grupos particulares de personas.
● Los formularios varían según la edad, el lugar de origen y la afinidad con los deportes que tiene
el usuario.
● El número máximo de cuestionarios a responder es de 3.
● Los usuarios que son originarios de América Latina responden el cuestionario sobre hábitos
alimenticios.
● Los usuarios que NO son originarios de América Latina no responden el cuestionario de hábitos
alimenticios.
● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad.
● Los usuarios originarios de América Latina entre 30 y 59 años responden el cuestionario de
experiencia laboral.
● Los usuarios originarios de América Latina de 60 años y más responden el cuestionario de
actividades recreativas.
● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años responden
el cuestionario de atletismo.
● Los usuarios originarios de América Latina que tienen afinidad por los deportes y que tienen 60
años o más responden el cuestionario de natación.
● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de
Deportes en General.
● El usuario debe ingresar por consola sus características (lugar de origen, edad y afinidad por los
deportes).
● Programa un mensaje que indique el número de cuestionarios a responder y cuáles son."""
bienvenida = ("***** bienvenido a la seccion de encuestas, por favor elija una de las siguientes opciones:  *****")
print(bienvenida)
print("-"*100)
origen = input("¿es ud originario de america latina?: ")
caracteres = len(origen)
tipo = origen.isalnum()
if tipo == True:
    if caracteres < 2:
        print("debe eingresar 2 caractres")
    elif caracteres > 3:
        print("binvenido usuario")    
    else:
        print ("vuelva a intenatrlo" )    
else:
    print("error, valor incorrecto")        

while True:
    try:
        edad = int(input(" ingrese su edad: "))
        break
    except ValueError:
        print("ingrese solo numeros enteros positivos del 18 al 100")
        
afinidad = input("tiene afinidad con los deportes: ")        
caracteres = len(afinidad)
tipo = afinidad.isalnum()
if tipo == True:
    if caracteres < 2:
        print("debe eingresar 2 caractres")
    elif caracteres > 2:
        print("binvenido usuario")    
    else:
        print ("vuelva a intenatrlo" )    
else:
    print("error, valor incorrecto")          
print("-"*100)
print(f"¡su origen es latinoamerica! : {origen}")
print(f"¡su edad es!  : {edad}")
print(f"afinidad con los deportes : {afinidad}")
print("-"*100)

if  origen.upper() =="SI":
    print("te corresponde el cuestinario de habitos alimenticios" )
else:
    print("este cuestinorio no es para ti")
   
if  edad == 18 >= 29:
   print("te corresponde el cuestinoraio de empleabilididad")
elif  edad == 30 >= 59:
   print("te corresponde el cuestinoraio de expecienci laboral")
elif edad == 60>=100:
   print("te corresponde el cuestinario de actividades recreativas")
   
if  afinidad.upper() =="SI" and edad == 30 or edad < 59:
    print("te corresponde el cuestionario de atletismo")
if  origen.upper() =="SI" and edad == 30 or edad < 59:
    print("te toca responder le cuertinorio natacion")
      
elif afinidad.upper() =="No":
    print("te toca responder le cuertinorio de deportes en general")          
       
    
fin =( "*" *42 +"fin del programa" +"*" *42 )      
print(fin)
    
    



