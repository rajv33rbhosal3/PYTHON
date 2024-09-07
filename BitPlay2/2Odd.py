def TO(arr,size):
    x2 = arr[0]
    x = 0
    y = 0
    for i in range(1,size):
        x2 = x2^arr[i]
    SB = x2 & ~(x2-1)
    for i in range(size):
        if (arr[i]&SB):
            x = x^arr[i]
        else:
            y = y^arr[i]
    print("Two odd elements are",x,"&",y)
arr = []
arr_size = int(input("Enter size of array"))
for i in range(0,arr_size):
    z = int(input("Enter a element"))
    arr.append(z)
print("Two Odd")
