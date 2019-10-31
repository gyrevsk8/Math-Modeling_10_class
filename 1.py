def day(a,b,c):
    """
    определяет день недели по дате
    на вход день, код месяца,год для 21 века
    """
    j=(6+(c%100)+(c%100)/4)%7
    k=(a+b+j)%7
    if k>=1 and k<2:
        return 'ponedelnik'
    elif k>=2 and k<3:
        return 'vtornik'
    elif k>=3 and k<4:
        return 'sreda'
    elif k>=4 and k<5:
        return 'chetverg'
    elif k>=5 and k<6:
        return 'pyatnica'
    elif k>=6 and k<7:
        return 'subboteya'
    elif k>=7:
        return 'voskresenie'
    else:
        return k
n=day(31,1,2019)
print(n)