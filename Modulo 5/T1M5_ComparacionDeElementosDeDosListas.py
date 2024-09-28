def mostrar_elementosComunes(A,B):
    for i in A:
        if i in B:
            print(i,end=' ')

def mostrar_elementosEnBNoEnA(A,B):
    for i in A:
        if i not in B:
            print(i,end=' ')
            
def mostrar_elementosEnBNoEnA(A,B):
    for i in B:
        if i not in A:
            print(i,end=' ')

mostrar_elementosComunes([1,2,3],[0,2,3])