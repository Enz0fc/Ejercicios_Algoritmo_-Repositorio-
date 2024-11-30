#ordenar por seleccion
def ordenarPorSeleccion(lista):
    for i in range(len(lista)):
        min=i
        for j in range(i+1,len(lista)):
            if lista[min]<lista[j]:
                min=j
        aux=lista[i] #se guarda el elemento de la lista de indice i en una variable auxiliar
        lista[i]=lista[min] #se cambia el elemento mayor/menor con el anterior elemento 
        lista[min]=aux #el elemento de la lista de indice i se considera como el nuevo minimo de la sublista
    return lista