"""Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones,
para simular el funcionamiento de tu aplicación.
Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su aplicación.
En cada diccionario, integre características como: edad, género y otras características particulares de su
aplicación.
Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico.
Integre al menos cinco características.
Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre
cada usuario (en el caso de ejemplo: de cada junta de vecinos).
¿Qué problemas encontró con esta forma de almacenar la información?
Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas
las juntas de vecinos.
Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.
Imprima en pantalla la fecha de incorporació"""
from datetime import datetime

lisatadojuntavecinos = [
{
'jjvv:01'                        
'id_usuario' : '*',
'Nombre' :'arnaldo',
'Apellido' :'Filosa',
'Edad' :'25',
'Genero' :'Masculino',
'Estadocivil' :'Soltero',
'Hijos' :'4',
'fechaingreso' : '05-12-2021',
},
                                        {
'jjvv:02'                        
'id_usuario': '*',
'Nombre'   : 'Margarita',
'Apellido' : 'Cortes',
'Edad'     : '55',
'Genero'   : 'Femenino',
'Estadocivil': 'Soltera',
'Hijos'    :  'Ninguno/a',
'fechaingreso' : '05-12-2021',
},
                    {
'jjvv:03'                        
'id_usuario' : '*',
'Nombre' : 'pamela',
'Apellido' : 'arnaldo',
'Edad' :'35',
'Genero' : 'Femenino',
'Estadocivil' : 'casada',
'Hijos' : '3',
'fechaingreso' : '05-12-2021',
},
                    {
'jjvv:04'                        
'id_usuario' : '*',
'Nombre' : 'yoslena',
'Apellido' : 'sanchez',
'Edad' :'65',
'Genero' : 'Femenino',
'Estadocivil' : 'Viuda',
'Hijos' : 'Ninguno/a',
'fechaingreso' : '05-12-2021',
},                                                         
                    {
'jjvv:05'                        
'id_usuario' : '*',
'Nombre' : 'Margarita',
'Apellido' : 'Stone',
'Edad' :'45',
'Genero' : 'Femenino',
'Estadocivil' : 'Divorsiada',
'Hijos' : '8',
'fechaingreso' : '05-12-2021',
},
                    {
'jjvv:06'                        
'id_usuario' : '*',
'Nombre' : 'Rchard',
'Apellido' : 'Malcond',
'Edad' :'35',
'Genero' : 'Masculino',
'Estadocivil' : 'Casado',
'Hijos' : 'Ninguno/a',
'fechaingreso' : '05-12-2021',
},
                    {
'jjvv:07'                       
'id_usuario' : '*',
'Nombre' : 'Andres',
'Apellido' : 'Torres',
'Edad' :'85',
'Genero' : 'Masculino',
'Estadocivil' : 'Casado',
'Hijos' : '5',
'fechaingreso' : '05-12-2021',
},
]
rescata_id = []
i = 0
print('-'*25 + " imprime listado completo de usuarios y sus caracteristicas " + '-'*25)
print('\tNombre \t Apellido \t Edad \t Genero\t Estadocivil\t Hijos ')
#print('   Nombre     Apellido    Genero     Edad  Estadocivil    hijos Fecha Ingreso')
for item in lisatadojuntavecinos:
    print('   '  + item['Apellido'],
          '    ' + item['Genero'],
          '    ' + item['Edad'],
          '    ' + item['Estadocivil'],
          '    ' + item['Hijos'],
          '    ' + item['fechaingreso'])

for i in range (0, len(lisatadojuntavecinos)):
    print(lisatadojuntavecinos[i][0])





#for clave in lisatadojuntavecinos:
    #print(clave)
    #print(clave, ":", lisatadojuntavecinos[clave])
    
    
    
#for i in  lisatadojuntavecinos:
    #for k,v in i.items():
        #print(k, '  \t' , v[0], '  \t  , 'v[1], '  \t')  
#menu =True

#while menu:
    
   # menu = int(input("menu principal: \n 1-Agregar clientle\n 2-Agregar \n"))
  #  opcion =""
  #  while opcion not in ("1","2"):
     #   opcion = input ("->")      
    
    

#for clave in jjjv1: #muestras las claves de diccionarios
    #print(clave,":",jjjv1,[clave])

#vista_claves = lisataojuntavecino.keys()  #muestra las llaves de los diccionarios
#vista_claves = list(jjjv1.keys()) #convierte las claves en lista
#vista_claves = jjjv1.keys()
#for clave in vista_claves:
#print(vista_clave)


#print(jjjv1.values()) #visualiazion de los valores 

#if 50 in jjjv1.values(): #busca un valor en diccionario
   # print("esta en el diccionario")






        