n=input()
contador=0
contador2=0

for i in str(n):
    if i=='4' or i=='7':
        contador+=1
    elif i!='7' or i !='7':
        contador2+=1
if contador2==0:
    print('El numero es de la suerte')
elif contador==4 or contador==7:
    print('El numero es casi de la suerte')
else:
    print('Ninguno')