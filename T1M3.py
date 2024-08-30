def MCD(a,b):
    n1=max(a,b)
    n2=min(a,b)
    while True:
        r=n1%n2
        if r!=0:
            n1=n2
            n2=r
        else:
            return(n2)
            break

def validacion(x):
    try:
        numero = int(x)
        if numero > 0:
            return numero
        else:
            return None
    except ValueError:
        return None


while True:
    N = input()
    N = validacion(N)
    if N is not None:
        break


contador = 1
mcdActual = None
argumentos = ""

while contador <= N:
    while True:
        numero = input()
        numero_validado = validacion(numero)
        if numero_validado is not None:
            if mcdActual is None:
                mcdActual = numero_validado  
            else:
                mcdActual = MCD(mcdActual, numero_validado)  
            argumentos += str(numero_validado)  
            if contador < N:
                argumentos += ", "  
            contador += 1
            break


print(f"El mcd({argumentos}) es: {mcdActual}")
