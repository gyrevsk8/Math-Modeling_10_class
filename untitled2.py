import math
a=math.radians(30)
b=math.tan(a)
d=b*b
h=100
from math import pi 
from const import g,plank,bolcman,eler
alph=pi/3
cc=math.cos(alph)
n=math.cos(alph)**2
v=((g*h*d)/(2*n*(1-b*cc)))**0.5
print(v)
spi=pi**0.5
T=200
J=300
X=((2/spi)*(plank/((bolcman*T)**(2/3))*(eler**(-J/bolcman*T))*J**(T/2)))
print(X)

 



