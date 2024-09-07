def ON(a):
    r = 0
    for i in a:
        r = r^i
    return r
a = []
n = int(input("Enter a number : "))
while n :
    b = int(input("Enter a number : "))
    a.append(b)
    n = n-1
print("\nOdd num is ",ON(a))