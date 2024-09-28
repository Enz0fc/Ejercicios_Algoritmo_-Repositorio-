
def mostrar_elementosComunes(A,B):
    '''Función que muestra los elementos comunes de A y B'''
    #Implementar de acuerdo a lo solicitado
    for i in A:
        if i in B:
            print(i,end=' ')
def mostrar_elementosEnANoEnB(A,B):
    '''Función que muestra los elementos de A que no están en B'''
    #Implementar de acuerdo a lo solicitado
    for i in A:
        if i not in B:
            print(i,end=' ')

def mostrar_elementosEnBNoEnA(A,B):
    '''Función que muestra los elementos de B que no están en A'''
    #Implementar de acuerdo a lo solicitado
    for i in B:
        if i not in A:
            print(i,end=' ')