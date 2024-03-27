for i in range(0,7):
    for j in range(0,7):
        if i==0 or i==6 or i==j or i+j==6:
            print(" *",end="")
        else:
            print("  ",end="")
    print()