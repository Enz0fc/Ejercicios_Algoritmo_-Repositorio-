
def estaEnLaLista_Salto(A,x,salto):
    '''Función que indica con True si un elemento x está en la lista, y
    False en caso contrario. El entero "salto" indica el incremento en 
    el proceso de recorrer la lista'''
    #Implementar de acuerdo a lo solicitado
    for i in range(0,len(A),salto):
        if x==A[i]:
            respuesta=True
            break
        else:
            respuesta=False
    return respuesta
def contarElementosDistintos(A):
    '''Función que devuelve la cantidad de elementos distintos en un 
    vector de N elementos'''
    #Implementar de acuerdo a lo solicitado
    B=[]
    for i in A:
        if A.count(i)>=1 and i not in B:
            B.append(i)
    return len(B)
def obtenerListaL2(L1):
    '''Función que obtiene y retorna la lista L2 según las especificaciones del problema
    Obs: si no lo considera necesario, puede optar por no emplear las funciones anteriores'''
    #Implementar de acuerdo a lo solicitado
    L2=[]
    contador=[]
    for i in L1:
        if L1.count(i)>=1 and i not in L2:
            L2.append(i)
    for i in L2:
        contador.append(L1.count(i))
    k=0
    for i in contador:
        L2.insert(k+1,i)
        k+=2
    return L2