mensaje='O ARRETA** FC DMSIA*LRADYR CE*RAEISNNAI*GL  ASET**TSIAFJ MS*I NFCSDSC*PECRIAO A*AA E  UNM*CIICEEACT*8204975613'

def codificar(mensaje, clave):
    '''
    Permite realizar la codificación de acuerdo al método expuesto. Esta función recibe dos cadenas: mensaje y clave. 
    mensaje contiene el mensaje a codificar y clave contiene la clave para realizar la codificación. 
    La función debe retornar una cadena con el mensaje codificado.
    '''
    #Implementar de acuerdo a lo solicitado
    
    #se llena hasta que tenga 100 caracteres
    if len(mensaje)<100:
        mensaje=mensaje+'*'*(100-len(mensaje))
    
    matriz=[]
    contador=0
    #se guarda el mensaje de 100 caracteres en la matriz
    for i in range(10):
        fila=[]
        for j in range(10):
            fila.append(mensaje[contador])
            contador+=1
        matriz.append(fila)
    #se codifica el mensaje con los elementos de la matriz
    mensaje=''
    for columna in str(clave):
        for fila in range(10):
            mensaje+=matriz[fila][int(columna)]
    mensaje+=str(clave)
        
        
    return mensaje

def decodificar(mensCod):
    '''
    Permite realizar la decodificación (proceso inverso para recuperar el mensaje original) de acuerdo al método expuesto. 
    Esta función recibe una cadena mensCod que contiene el mensaje codificado, y debe retornar una cadena 
    con el mensaje original (decodificado).
    '''
    #Implementar de acuerdo a lo solicitado
    matriz=[[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10]
    clave=mensCod[len(mensCod)-10:]
    mensaje=mensCod[0:len(mensCod)-10]
    resultado=''
    #descripta el mensaje y lo carga en la matriz
    contador=0
    for repeticiones in range(10):
        for fila in matriz:
            fila[int(clave[repeticiones])]=mensaje[contador]
            contador+=1
    #imprime los elementos de la matriz mostrando el mensaje
    for i in matriz:
        for j in i:
            resultado+=j
    #eliminamos los asteriscos que rellenan la matriz
    resultado=resultado[:len(resultado)-resultado.count('*')]
            
    return resultado

print(decodificar(mensaje))
