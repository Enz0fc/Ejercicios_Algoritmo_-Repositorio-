examen=float(input('Ingrese la nota del examen: '))*0.7
leccion=float(input('Ingrese la nota de la leccion: '))*2
t1=float(input('Ingrese la nota de la primera tarea: '))
t2=float(input('Ingrese la nota de la segunda tarea: '))
t3=float(input('Ingrese la nota de la tercera tarea: '))
t4=float(input('Ingrese la nota de la cuarta tarea: '))

tarea=((t1+t2+t3+t4)/4)
print('El puntaje sobre la escala es:',{examen+leccion+tarea})