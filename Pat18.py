for i in range(6):
    alpha =0
    for j in range(5-i):
            print("  ",end="")
    for k in range(2*i -1):
            print(chr(65+alpha),end=" ")
            alpha +=1
    print()