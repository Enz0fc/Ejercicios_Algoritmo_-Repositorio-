d=float(input())
m=float(input())

if m==2:
    a= float(input())
    if a%4!=0 or (a%100==0 and a%400!=0):
        n=28
    elif (a%4!=0 or (a%100==0 and a%400!=0)) and d>28:
        print('No es una fecha valida!!')
    else:
        n=29
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    n=31
    a=float(input())
else:
    n=30
    a=float(input())


if d<=0 or m<=0 or a<0 or d>n or m>12 or d%round(d)!=0 or m%round(m)!=0 or (a<0 and a%round(a)!=0) or a%round(a)!=0 :
    print('No es una fecha valida!!')
elif d==n and m==12:
    print(f'01/01/{int(a+1):04}')
elif d==n:
    print(f'01/{int(m+1):02}/{int(a):04}')
else:
    print(f'{int(d+1):02}/{int(m):02}/{int(a):04}')
    