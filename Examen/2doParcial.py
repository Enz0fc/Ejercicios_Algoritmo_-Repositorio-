import random


def ordenarMatriz(matriz):
#se almacena los valores en una lista para ordenarlos ahi
    listaAordenar=[]
    for i in matriz:
        for j in i:
            listaAordenar.append(j)
    #se ordena la lista de menora a mayor
    for i in range(len(listaAordenar)):
        actualizado=i
        for j in range(i+1,len(listaAordenar)):
            if listaAordenar[actualizado]>listaAordenar[j]:
                actualizado=j
        aux=listaAordenar[i] 
        listaAordenar[i]=listaAordenar[actualizado] 
        listaAordenar[actualizado]=aux 
    #la lista ya esta ordenada

    #se actualiza la matriz desordenada ordenandola como se requiere
    for i in range(n):
        #para columna par
        if i%2==0:
            list=listaAordenar[m*i:m*i + m]
            for j in range(m):
                matriz[j][i]=list[j]
        #para columna impar
        else:
            list=listaAordenar[m*i:m*i + m]
            for j in range(m):
                matriz[m-j-1][i]=list[j]
    #retorna la matriz ordenada
    return matriz

#-----------------------------PROGRAMA PRINCIPAL----------------------------------------
m=int(input('Ingrese la cantidad de filas de la matriz: '))
n=int(input('Ingrese la cantidad de coumnas de una matriz: '))


matriz=[]
for i in range(m):
    filas=[]
    for i in range(n):
        filas.append(random.randint(0,100))
    matriz.append(filas)
print(f'Se a creado una matriz de {m} filas y {n} columnas\n')
#mostrar matriz en pantalla sin ordenar
print('Matriz sin ordenar\n')
for fila in matriz:
    linea=''
    for columna in fila:
        linea+=str(columna)+'\t'
    print(linea.strip()+'\n')
    
#ordenamos la matriz con la funcion creada
ordenarMatriz(matriz)
#se muestra en pantalla dicha matriz
print('\nMatriz ordenada\n')
for fila in matriz:
    linea=''
    for columna in fila:
        linea+=str(columna)+'\t'
    print(linea.strip()+'\n')
    


