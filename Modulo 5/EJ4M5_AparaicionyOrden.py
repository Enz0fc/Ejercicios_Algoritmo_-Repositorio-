A=[3,4,1,2,3,3]

def nroApariciones(x,A):
    contador=0
    for i in A:
        if i==x:
            contador+=1
    return contador

def elementoQueMenosAparece(A):
    elementoQueMenosAparece=A[0]
    for i in A:
        if nroApariciones(i,A)<nroApariciones(elementoQueMenosAparece,A):
            elementoQueMenosAparece=i
    return elementoQueMenosAparece

def estaOrdenadoNoDesc(A):
    for i in range(1,len(A)):
        if A[i]>=A[i-1]:
            resultado=True
        else:
            resultado=False
            break
    return resultado
