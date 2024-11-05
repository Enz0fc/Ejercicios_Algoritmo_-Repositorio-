def esDeAltaSeguridad(contrasenha):
    #se guardan los simbolos que se requieren en la contrasenha
    simbolosrequeridos='*$%-?!#'
    #la primera prueba es ver si tiene mas de 12 caracteres
    if len(contrasenha)<12:
        retorno=False
    #si tiene mas de 12 caracteres se controla que cumpla con los requerimientos de mayusculas minusculas numeros y simbolos
    else:
        mayusculas=0
        minusculas=0
        numericos=0
        simbolo=0
        for i in contrasenha:
            if i.isupper():
                mayusculas+=1
            if i.islower():
                minusculas+=1
            if i.isnumeric():
                numericos+=1
            if i in simbolosrequeridos:
                simbolo+=1
            #ya se ha contado la la cantidad de minusculas, mayusculas, numeros y simbolos
            #se realiza que cumpla con lo requerido
        if minusculas<3:
            retorno=False
        elif mayusculas<3:
            retorno=False
        elif numericos<2:
            retorno=False
        elif simbolo<1:
            retorno=False
        else:
            retorno=True
        #retorna el vaalor booleano correspondiente
        return retorno

#------------------------PROGRAMA PRINCIPAL--------------------------------------

clave=input('Ingrese su contraseña: ')
#se realiza el control de la contrasenha y muestra en pantalla si la clave es o no de alta seguridad
if esDeAltaSeguridad(clave):
    print('La contraseña ingresada es de alta seguridad')
else:
    print('La contraseña ingresada NO es de alta seguridad')