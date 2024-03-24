for i in range(5,0,-1):
    for k in range(0,5-i):
        print(" ",end="")
    for j in range(0,i):
        print(chr(69-(5-(i-j))),end=" ")
    print()
