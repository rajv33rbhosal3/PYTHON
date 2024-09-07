def Nob(n):
    once = 0
    zero = 0
    while n:
        if n&1==1:
            once = once+1
        else:
            zero = zero+1
        n >>= 1
    print("Number of once = ",once,"\nNumber of zeros = ",zero)
num = int(input('Enter a number : '))

Nob(num)
