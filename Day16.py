for i in range(7):
    for j in range(7):
        if i==j or i==3 or j==3 or i+j==6:
            print("* ",end="")
        else:
            print("  ",end="")
    print()