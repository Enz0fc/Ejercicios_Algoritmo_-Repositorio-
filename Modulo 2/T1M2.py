import math

a=int(input())
b=int(input())
c=int(input())
det=(b**2)-(4*a*c)

if det>=0:
    print('Las raices son:')
    print(f"x1 = {(-b+math.sqrt(det))/(2*a):.3f}")
    print(f"x2 = {(-b-math.sqrt(det))/(2*a):.3f}")
else:
    print('Las raices son:')
    print(f'x1 = {(-b/2*a):.3f} + {(math.sqrt(det*-1)/2*a):.3f}j')
    print(f'x2 = {(-b/2*a):.3f} - {(math.sqrt(det*-1)/2*a):.3f}j')
