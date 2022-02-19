#Creación de un entorno virtual.
#● Identificar la dirección de la carpeta donde están los archivos del entorno virtual.
#● Activación del entorno virtual creado.
#● Investigar las ventajas que tenemos al utilizar un entorno virtual en el desarrollo de nuestro
#proyecto.
#● Como grupo, deberán definir un listado de 5 productos con su respectivo valor unitario.
#● Deberán crear un archivo .py el cual deberá solicitar ingresar una cantidad por cada producto
#(definido de la lista).
#● Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto.
#● Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado.
#● Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA).

producto=[["hamburgesa1",1500],["papasfrtias2",990],["vasobebida3",1490],["nuggetspollo4",850],["fagitas5",1490]]
hamburgesa=input("cantidad hamburgesa quiere de 1500: ")
papasfritas=input("papasfritas de 990: ")
vasobebida=input("vasobebida 990: ")
nuggetspollo=input("nuggetpollo 1490: ")
fagitas=input("fagitas 1490: ")

uno=productos[0][1]
dos=productos[1][1]
tres=productos[2][1]
cuatro=productos[3][1]
cinco=productos[4][1]

uno = int(hamburgesa)*uno
dos = int(papasfritas)*uno
tres = int(vasobebida)*uno
cuatro|= int(nuggetspollo)*uno
cinco|= int(fagitas)*uno
totalneto=uno+dos+tres+cuatro+cinco

totaliva=totalneto*19/100
print(taotaliva)
