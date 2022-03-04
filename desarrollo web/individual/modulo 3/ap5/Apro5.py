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

socios_juntaVecinos = [ 
    {'id_jjvv': 'JJVV_01', 'id_unico': '-', 'nombre_usuario': 'Usuario A','edad': 25, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
    {'id_jjvv': 'JJVV_01', 'id_unico': '-', 'nombre_usuario': 'Usuario B','edad': 30, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
    {'id_jjvv': 'JJVV_01', 'id_unico': '-', 'nombre_usuario': 'Usuario C','edad': 40, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
    {'id_jjvv': 'JJVV_01', 'id_unico': '-', 'nombre_usuario': 'Usuario D','edad': 42, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
    {'id_jjvv': 'JJVV_02', 'id_unico': '-', 'nombre_usuario': 'Usuario E','edad': 36, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
    {'id_jjvv': 'JJVV_02', 'id_unico': '-', 'nombre_usuario': 'Usuario F','edad': 33, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
    {'id_jjvv': 'JJVV_02', 'id_unico': '-', 'nombre_usuario': 'Usuario G','edad': 45, 'genero': 'F', 'antiguedad': '0', 'fec_incorporacion': '12-12-12'},
]

rescata_id = []
i = 0

ingreso_socio = datetime(2021, 7, 25)
today = datetime.now()
rectifica = datetime(today.year, ingreso_socio.month, ingreso_socio.day) >= today
permanencia =format(today.year - ingreso_socio.year - rectifica)

print("LISTADO CON DICCIONARIO DE CADA SOCIO JUNTA VECINAL")
print('   cod.JJ |    id |   Nombre   |  Edad | S | Ant. |Fecha Ingreso')
for item in socios_juntaVecinos:
    print('   ' + item['id_jjvv'],
          '   ' + item['id_unico'],
          '    ' + item['nombre_usuario'],
          '    ' + str(item['edad']),
          '    ' + item['genero'],
          '    ' + item['antiguedad'],
          '    ' + item['fec_incorporacion'])


    socios_juntaVecinos[i].update({'id_unico': 'id_' + str(i), 'nombre_usuario': 'Nombre' + str(
        i), 'antiguedad': permanencia, 'fec_incorporacion': '08-15-2020'})
    i = i + 1

print(" LISTADO CON DICCIONARIO DE CADA SOCIO JUNTA VECINAL, SE AGREGAN DATOS")
print('   cod.JJ     id    Nombre     Edad  S  Ant. Fecha Ingreso')
for item in socios_juntaVecinos:
    print('   ' + item['id_jjvv'],
          '   ' + item['id_unico'],
          '    ' + item['nombre_usuario'],
          '    ' + str(item['edad']),
          '   ' + item['genero'],
          '    ' + item['antiguedad'],
          '    ' + item['fec_incorporacion'])

print(" LISTADO CON DICCIONARIO DE CADA SOCIO JUNTA VECINAL, FECHA INGRESO")
print('  id      Nombre    Fecha Ingreso')
for item in socios_juntaVecinos:
    print('   ' + item['id_unico'],
          '    ' + item['nombre_usuario'],
          '    ' + item['fec_incorporacion'])
