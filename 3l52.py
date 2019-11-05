import numpy as np
import matplotlib.pyplot as plt
def krug(R=1,a=3,b=2):
    x=np.arange(-10,10,0.01)
    y=np.arange(-10,10,0.01)
    X,Y=np.meshgrid(x,y)
    #Y=np.meshgrid(x,y)
    f=X**2+Y**2
    plt.contour(X,Y,f,levels=[R])
    d=X**2/a**2+Y**2/b**2
    plt.contour(X,Y,d,levels=[1])
    plt.show()
krug(10)    