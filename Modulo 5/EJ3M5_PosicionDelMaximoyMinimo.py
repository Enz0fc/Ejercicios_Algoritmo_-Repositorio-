def pos_maximo(V):
    mayorActual=V[0]
    for i in range(len(V)):
        if V[i]>=mayorActual:
            mayorActual=V[i]
            posicion=i
    return posicion

def pos_minimo(V):
    menorActual=V[0]
    for i in range(len(V)):
        if V[i]<=menorActual:
            menorActual=V[i]
            posicion=i
    return posicion

print(pos_maximo([1,6,10,6,73,1,73,16]))
print(pos_minimo([2,8,10,6,74,1,34,16,1,5]))