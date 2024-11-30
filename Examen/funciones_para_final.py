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

#la funcion retorna una lista donde el primer elemento la cantidad de salario (un entero) y el segundo elemento la moneda (una cadena)
def obtenerDatosSalario(CantidadMoneda):
    cantidad=''
    moneda=''
    for i in CantidadMoneda:
        if i.isnumeric() or i=='.': #se controla que sea un entero o separador de miles para buscar la cantidad del salario
            if i.isnumeric():
                cantidad+=i
            else:
                pass
        else: #en caso de no ser entero ni separador de miles, se asume que es la moneda indicada al final
            moneda+=i
    #se crea crea finalmente la variable moneda la cual debe devolver el programa
    if moneda.lower()=='gs':
        moneda='Guaranies'
    elif moneda=='$':
        moneda='Dolares'
    elif moneda.lower()=='R$':
        moneda='Reales'
    else:
        moneda='Otro'
    return [int(cantidad),moneda]