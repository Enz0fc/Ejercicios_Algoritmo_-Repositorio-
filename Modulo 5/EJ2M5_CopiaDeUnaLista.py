def copiarVector(A):
    
    return A[:]

def leerVector(A):
    lista=[]
    for i in A:
        lista.insert(0,i)
    return lista

LISTA=[1,2,3,4]
print(leerVector(LISTA))

