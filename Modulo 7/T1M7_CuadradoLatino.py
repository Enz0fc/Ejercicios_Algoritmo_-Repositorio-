A=[[0,1,2],[2,0,1],[1,2,0]]


def controlarRepeticion(lista):
    #True si no se repite, False si se repite alguno
    for i in lista:
        if lista.count(i)==1:
            resultado=True
        else:
            return False
    return resultado
        
def esCuadradoLatino(A):
    '''
    Esta función devuelve True si la matriz A es un cuadrado latino,
    y False en caso contrario
    '''
    #Implementar de acuerdo a lo solicitado
    n=len(A)
    for i in A:
        for j in i:
            if j>n:
                return False
    
    for i in A:
        if not controlarRepeticion(i):
            return False
    
    try:
        for elemento in A[0]:
            aux=[]
            for lista in A: 
                aux.append(lista.index(elemento))
            if not controlarRepeticion(aux):
                return False
    except:
        return False
    return True

print(esCuadradoLatino(A))