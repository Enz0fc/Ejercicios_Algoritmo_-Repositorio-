def cargarLista(N):
    lista=[]
    contador=1
    while contador <= N:
        elemento=int(input())
        if elemento not in lista:
            lista.append(elemento)
            contador+=1
    return lista
def ordenarAscendente(lista):
    for i in range(len(lista)):
        min=i
        for j in range(i+1,len(lista)):
            if lista[min]>lista[j]:
                min=j
        aux=lista[i] 
        lista[i]=lista[min] 
        lista[min]=aux 
    return lista
def ordenamientoEspecial(A):
    B=ordenarAscendente(A[:])
    N=len(A)
    resultado=['valor']*N
    j=0
    
    if N%2==0:
        rango=N//2
    else: 
        rango=(N//2)+1
    
    for i in range(rango):
        resultado.insert(i,B[j])
        resultado.remove('valor')
        try:
            resultado.insert(N-(1+i),B[j+1])
            resultado.remove('valor')
        except:
            pass
        j+=2
        A.clear()
        for i in resultado:
            A.append(i)
    

lista=[12,3,4,5,-1,20]
ordenamientoEspecial(lista)
print(lista)
        