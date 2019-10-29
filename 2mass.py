import numpy as np
import random as rnd
b=np.eye(6)
for i in range (0,5,1):
    b[i]=rnd.random()
def multy(a):
    """
    перемножает элементы массива
    """
    k=0
    for i in range(0,5,1):
        k=k+a[i]*a[i+1]
    return(k)
print(multy(b))   
