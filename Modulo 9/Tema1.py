
nombreArch=input("Ingrese el nombre del archivo de entrada: ")
#nombreArch='alumnos.txt'
fechaRef=input("Ingrese la fecha de referencia: ")
#fechaRef='20220516'

arch=open(nombreArch,"r")

lineas=arch.readlines()
arch.close()
datos=[]
fecha=int(fechaRef)
for linea in lineas: 
    dato=linea.split() 
    dato[0]=int(dato[0])
    dato[5]=dato[5].strip()
    dato[5]=int(dato[5])
    edad=int((fecha-int(dato[4]))/10000)
    dato.append(edad)
    datos.append(dato)


franjas=["< 18","18-20","21-24","25-30","> 30"]
reporte=[]
for i in range(len(franjas)): 
    reporte.append([0]*3)


for alumno in datos:   
    if alumno[5]>=2015: 
        if alumno[3]=="M":
            col=0
        else:
            col=1

        edad=alumno[6]
        if edad<18:  
            fil=0
        elif edad<21:
            fil=1
        elif edad<25:
            fil=2
        elif edad<=30:
            fil=3
        else:
            fil=4
        reporte[fil][col]=reporte[fil][col]+1 
        reporte[fil][2]=reporte[fil][2]+1 

archSalida=open('reporte.txt','w')
archSalida.write('Reporte\n')
archSalida.write("Franja\tM\tF\tTotal\n")
for i in range(len(reporte)):
    archSalida.write(franjas[i]+"\t")
    for j in range(len(reporte[i])):
        archSalida.write(str(reporte[i][j])+'\t')
    archSalida.write('\n')
archSalida.close()

#alumno mas joven
alumnosFiltrados=[]
for alumnos in datos:
    if alumnos[5]>=2015:
        alumnosFiltrados.append(alumnos)
masJoven=alumnosFiltrados[0]
for alumno in alumnosFiltrados:
    if alumno[6]<masJoven[6]:
        masJoven=alumno

print('\nSe genero el reporte!!\n')
print("Los datos del alumno más joven son:")
for i in range(len(masJoven)-1):
    print(masJoven[i],end=" ")





