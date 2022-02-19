print("Ingrese el numero de estudiantes: ")
x=int(input())
print("---------------------------------------------")
a=1
trm=0
trk=0
tel=0
#Se crea un Diccionario estudiantes para asociar cada estudiante a una musica y una carrera
estudiantes={}
numeroe=1
#los arreglos musica y carrera son solo para ser mostrados en la seleccion
musica=dict(Rock=1,Regaeton=2,Salsa=3)
carrera=dict(Materiales=1,Electronica=2,Topografia=3)
 
print("---------------SELECCION MUSICAS----------------")
for j,k in musica.items():
    print(k,j)
 
print("---------------SELECCION CARRERAS----------------")
for l,m in carrera.items():
    print(m,l)
 
print("--------------------------------------------------")
#lee e ingresa los valores al numero de estudiantes ingresado
while(x!=0):
    print("Estudiante numero "+str(numeroe)+" Digite su tipo de musica favorito")
    musicae=input()
    print("Estudiante numero "+str(numeroe)+" Digite su carrera")
    carrerae=input()
    estudiantes["estudiante"+str(numeroe)]=[musicae,carrerae]
    print("-----------------------------------------------")
    numeroe=numeroe+1
    x=x-1
 
#for para recorrer cuantos estudiantes se ingresaron
for g in estudiantes.keys():
    #cuantos escuchan regueton y estan en la carrera materiales
    if estudiantes["estudiante"+str(a)][0]=="2" and estudiantes["estudiante"+str(a)][1]=="1":
        trm=trm+1
    #cuantos escuchan rock
    if estudiantes["estudiante"+str(a)][0]=="1":
        trk=trk+1
    #cuantos escuchan electronica
    if estudiantes["estudiante"+str(a)][1]=="2":
        tel=tel+1
    #la variable a hace la iteracion de un estudiante a otro "estudiantes["estudiante"+str(a)]"
    a=a+1
 
print("-----------------------------------------------------")
 
print("Total Regueton Materiales: "+str(trm))
print("Total Rock: "+str(trk))
print("Total Electronica: "+str(tel))
