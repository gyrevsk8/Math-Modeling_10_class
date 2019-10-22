import numpy as np
from const import g
t=np.arange(0,5.01,0.01)
x0=0
v0=40
y0=0
for i in range(0,500,1):
    x=x0+v0*t[i]
    y=y0+v0*t[i]-((g*t[i]**2)/2)
    print(x)
    print(y)