import numpy as np
import matplotlib.pyplot as plt
def parabola(a=1,b=1,c=0):
    """risuet parabolu"""
    x=np.arange(-10,10,0.01)
    x[1000]=0.01
    y=a*x**2+b*x+c
    plt.plot(x,y,label='parabola')
    plt.legend()
    d=1/(x*3)
    plt.plot(x,d,label='giperbola')
    plt.legend()
    plt.show()
parabola()
