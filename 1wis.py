def god(a):
    """
    определяет високосность года
    """
    if a%4==0:
        if a%100==0:
            if a%400==0:
                print('Високосный')
            else:
                print('Невисокосный')
        else:
            print("Високосный")    
    else:
        print('Невисокосный')
print(god(2000))        
