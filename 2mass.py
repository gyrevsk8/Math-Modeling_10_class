import numpy as np
import random as rnd
b=np.eye(6)
for i in range (0,5,1):
    b[i]=rnd.randint(1,100)
def multy(a):
    """
    перемножает элементы массива
    на вход нужный массив
    """
    k=0
    for i in range(0,5,1):
        k=k+a[i]*a[i+1]
    return(k)
print(multy(b))   
