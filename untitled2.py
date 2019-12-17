import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,1000,0.01)
g=9.8066
def diff_func(z,t):
    y,omega=z
    dy_dt=omega
    domega_dt=-G*m/y**2
    return dy_dt,domega_dt
y0=6400000
G=6.674*10**(-11)
omega=0.05
k=0.3
m=5.97*10**24
l=1
z0=y0,omega
sol=odeint(diff_func,z0,t)
#plt.plot(sol[:,1],sol[:,0],'k')#черная дыра
#plt.plot(t,sol[:,0])#Синяя балда
plt.plot(t,sol[:,0])#оранжевая балда
#plt.plot(sol[:,0],t)#зеленая адлаб
plt.show
#y это радиус м масса земли