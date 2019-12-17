import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,7,0.01)
def diff_func(z,t):
    y,omega=z
    dy_dt=omega
    domega_dt=-np.sin(y)*omega-3*y*t+5
    return dy_dt,domega_dt
y0=0.01
omega=0.05
z0=y0,omega
sol=odeint(diff_func,z0,t)
plt.plot(sol[:,1],sol[:,0],'k')#черная дыра
plt.plot(t,sol[:,0])#Синяя балда
plt.plot(t,sol[:,1])#оранжевая балда
plt.plot(sol[:,0],t)#зеленая адлаб
plt.show