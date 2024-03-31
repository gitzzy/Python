for i in range(1,6):
    for j in range(1,6):
        if i+j>5:
            print(chr(58+i+j+i)+" ",end="")
        else:
            print("  ",end="")

    for k in range(1,6):
        if i+k<=2*i:
            print((i+k-1),"",end="")
        else:
            print("  ",end="")
    print()