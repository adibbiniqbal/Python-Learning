import math
a = int(input('enter a : '))
b = int(input('enter b : '))
c = int(input('enter c : '))
r1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
r2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
print('r1 = ', r1, ' r2 = ', r2)
