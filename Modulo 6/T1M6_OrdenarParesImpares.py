A = [6, 9, 10, 10, 6, 8, 3, 2, 1, 3, 7]
def ordenarMenorMayor(lista):
    for i in range(len(lista)):
        min=i
        for j in range(i+1,len(lista)):
            if lista[min]>lista[j]:
                min=j
        aux=lista[i] #se guarda el elemento de la lista de indice i en una variable auxiliar
        lista[i]=lista[min] #se cambia el elemento mayor/menor con el anterior elemento 
        lista[min]=aux #el elemento de la lista de indice i se considera como el nuevo minimo de la sublista
    return lista

def ordenarMayorMenor(lista):
    for i in range(len(lista)):
        min=i
        for j in range(i+1,len(lista)):
            if lista[min]<lista[j]:
                min=j
        aux=lista[i] #se guarda el elemento de la lista de indice i en una variable auxiliar
        lista[i]=lista[min] #se cambia el elemento mayor/menor con el anterior elemento 
        lista[min]=aux #el elemento de la lista de indice i se considera como el nuevo minimo de la sublista
    return lista

def ordenarPosParesEImpares(A):
    listaPares=[]
    listaImpares=[]
    #separa en lista distinta los de indice par e impar
    for i in range(len(A)): 

            if i%2==0:
                listaPares.append(A[i])
            else:
                listaImpares.append(A[i])
    #Limpia la lista para luego ordenar en ella los elementos solicitados
    A.clear()
    #Ordena de forma ascendete o descendente como solicita el problema
    ordenarMenorMayor(listaPares)
    ordenarMayorMenor(listaImpares)
    #Agrega a la lista los elementos en el orden correcto
    for i in range(len(listaImpares+listaPares)):
        if i%2==0:
            A.append(listaPares[i//2])
        else:
            A.append(listaImpares[i//2])

ordenarPosParesEImpares(A)

print(A)