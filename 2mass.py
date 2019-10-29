def multy(a):
    """
    перемножает элементы массива
    на вход нужный массив
    """
    k=1
    for i in range(0, len(a), 1):
        k=k*a[i]
    return k

a = [2, 3, 5]

print(multy(a))
