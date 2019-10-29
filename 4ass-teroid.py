import const as cc
def prop(m=1, v=1):
    """
    вероятность выживания от попадания астеройда
    на вход масса астеройда и скорость астеройда
    """
    E=m*v*v/2
    t=(E/(cc.massokean*4200))
    if t>50:
        print("vse умерло")
    elif t<50 and t>30:
        print('90% umerlo')
    else:
        print('bol')
print(prop(50,30000000000))        
    