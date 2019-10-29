import const as cc
def energy(v=1,h=1,m=1):
    """
    полная механическая энергия тела
    на вход Скрость, высота, масса
    """
    E=(m*v*v)/2+m*cc.g*h
    return(E)
j=energy(10,3,400)
print(j)