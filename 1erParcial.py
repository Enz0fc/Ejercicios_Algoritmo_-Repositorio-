def validacion(x):
    try:
        numero = int(x) #El numero a validar se convierte a entero y si es mayor a cero retorna True si lo es, y False si no lo es
        if numero > 0:
            return True
        else:
            return False
    except: #Si salta el error de que no es un numero entero (es decimal o cadena de texto por ej) retorna False
        return False
    

def multiplicacion_rusa(a,b):
    suma=0 #La suma que se emplea para el resultado es inicialmente cero
    while a!=0:
        if a%2!=0: #Si el numero de la primera columna NO es par, este se tiene en cuenta y se va sumando el numero de la segunda columna
            suma+=b
            
        #sigue la secuencia de dividir en tre dos el numero de la primera columna y duplicar el de la segunda hasta que el de la primea llegue a ser 1
        a=a//2
        b+=b
        
    #Retorna el resultado de la suma de los numeros de la segunda columna en los cuales el primer numero no era par    
    return suma
        


#Resolviendo el problema general
resultado=0
b=0

while True: 
    a=input()
    numero_validado=validacion(a) #Esta variable es tipo booleana, sirve para manipular el programa dependiendo de la validacion relizada
    
    if (numero_validado==False) and (b==0):
        print('El primer valor ingresado no es un numero entero y positivo')
        break
    
    if numero_validado: #Ingresa al if si la validacion retorna True
        
        if b==0: #Este if es para la primera iteracion, ya que b es inicialmente cero, aqui se guarda la variable ingresada inicialmente en a
            b=int(a)
        else:
            b=multiplicacion_rusa(int(b),int(a)) #Se agrega el int a los parametros para convertirlos a enteros ya que se usa la 
                                                         #variable del input el cual es una variable tipo string, el mismo trabajo se hace en la funcion de validacion.
 
            #Ahora b es la ultima multiplicacion realizada, el siguiente numero que se ingrese sera multiplicado por b (ultimo resultado)
 
    else: #Cuando se ingrese en el input un valor que no es entero y positivo saltara a este else y se imprimira el resultado correcto con los datos anteriormente ingresados
        print(f'La multiplicación de dichos números es: {b}')
        break