def cantDigitos(n):
    contador=0
    while n!=0:
        n=n//10
        contador+=1
    return(contador)

def potencia(a,b):
    return a**b

def sumaDigitosALaN(x,exponente):
    suma=0
    for i in range(cantDigitos(x)):
        suma+=((x%10**(i+1))//10**i)**exponente
    return suma

def esNroNarcisista(n):
    if sumaDigitosALaN(n,cantDigitos(n))==n:
        return True
    else:
        return False

def imprimirListaNrosNarcisistas(N):
    contador=1
    numero=1
    while contador<=N:
        if esNroNarcisista(numero):
            print(numero, end=' ')
            contador+=1
        numero+=1

def resolverProblemaGeneral():
    N=int(input())
    contador=1
    numero=1
    print('La lista de los 12 primeros numeros narcisistas es: ')
    while contador<=N:
        if esNroNarcisista(numero):
            print(numero, end=' ')
            contador+=1
        numero+=1
resolverProblemaGeneral()
