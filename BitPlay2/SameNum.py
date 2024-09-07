def CheckIfSame(n1,n2):
    if ((n1^n2)!=0):
        print("Numebr are not equal")
    else:
        print("NUmber are Equal")
n1 = int(input("Enter a number"))
n2 = int(input("Enter a number"))
CheckIfSame(n1,n2)