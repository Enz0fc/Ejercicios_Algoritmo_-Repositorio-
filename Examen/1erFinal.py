#la funcion retorna una lista donde el primer elemento la cantidad de salario (un entero) y el segundo elemento la moneda (una cadena)
def obtenerDatosSalario(CantidadMoneda):
    cantidad=''
    moneda=''
    for i in CantidadMoneda:
        if i.isnumeric() or i=='.': #se controla que sea un entero o separador de miles para buscar la cantidad del salario
            if i.isnumeric():
                cantidad+=i
            else:
                pass
        else: #en caso de no ser entero ni separador de miles, se asume que es la moneda indicada al final
            moneda+=i
    #se crea crea finalmente la variable moneda la cual debe devolver el programa
    if moneda.lower()=='gs':
        moneda='Guaranies'
    elif moneda=='$':
        moneda='Dolares'
    elif moneda.lower()=='r$':
        moneda='Reales'
    else:
        moneda='Otro'
    return [int(cantidad),moneda]
#la funcion retorna la cantidad de los salarios en forma de una lista para luego agregarla en orden al fichero que se creara
def obtenerCantidad(fichero):
    cantidad=[]
    lista=[] #esta lista auxiliar se usa para de ahi quitar las cantidades de la funcion que devuelve la cantidad con la moneda del salaro
    f=open(fichero,mode='r')
    for linea in f.readlines():
        lista.append(linea.split()[2]) #se agregan los nombres obtenidos de la planilla en el fichero
    f.close()
    for i in lista:
        cantidad.append(obtenerDatosSalario(i)[0])
    return cantidad
#la funcion retorna la moneda de los salarios en forma de una lista para luego agregarla en orden al fichero que se creara
def obtenerMoneda(fichero):
    moneda=[]
    lista=[] #esta lista auxiliar se usa para de ahi quitar las monedas de la funcion que devuelve la cantidad con la moneda del salaro
    f=open(fichero,mode='r')
    for linea in f.readlines():
        lista.append(linea.split()[2]) #se agregan los nombres obtenidos de la planilla en el fichero
    f.close()
    for i in lista:
        moneda.append(obtenerDatosSalario(i)[1])
    return moneda
#la funcion retorna los nombres en forma de una lista para luego agregarla en orden al fichero que se creara
def obtenerNombres(fichero):
    nombres=[]
    f=open(fichero,mode='r')
    for linea in f.readlines():
        nombres.append(linea.split()[0]) #se agregan los nombres obtenidos de la planilla en el fichero
    f.close()
    return nombres
#la funcion retorna las dependencias en forma de una lista para luego agregarla en orden al fichero que se creara
def obtenerDependencias(fichero):
    dependencias=[]
    f=open(fichero,mode='r')
    for linea in f.readlines():
        dependencias.append(linea.split()[-1])
    f.close()
    return dependencias
#la funcion retorna los apellidos en forma de una lista para luego agregarla en orden al fichero que se creara
def obtenerApellidos(fichero):
    apellidos=[]
    dependencias=[]
    f=open(fichero,mode='r')
    for linea in f.readlines():
        apellidos.append(linea.split()[1])
    f.close()
    return apellidos

#IMPORTANTE: LA FUNCION OBTENER SALARIO SE UTILIZA DENTRO DE LAS FUNCIONES obtenerCantidad y obtenerMoneda!!!

#Programa Principal------------------------------------------------


#guardamos en listas las columnas a agregar en el fichero solicitado 
campos=['Nombre','Apellido','Cantidad','Moneda','Dependencia']
nombres=obtenerNombres('empleados.txt')
apellidos=obtenerApellidos('empleados.txt')
cantidades=obtenerCantidad('empleados.txt')
monedas=obtenerMoneda('empleados.txt')
dependencias=obtenerDependencias('empleados.txt')

#se crea un fichero con el nombre empleados_Mod.txt con el siguiente fomato
#Nombre Apellido Cantidad Moneda Dependencia
f=open('empleados_Mod.txt',mode='w')
#se escriben los campos en la primera fila
for campo in campos:
    f.write(campo+'\t')
f.write('\n')
for columna in range(len(nombres)):#se realiza la accion de escribir la fila tantas veces como la cantidad de elementos en la lista nombres la cual tiene misma cantidad de elementos que las otras listas de datos
    f.write(f'{nombres[columna]}\t{apellidos[columna]}\t{cantidades[columna]}\t{monedas[columna]}\t{dependencias[columna]}\n')
f.close