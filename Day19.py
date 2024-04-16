for i in range(5):
    for k in range(4):
        for j in range(5):
            if i==j or i+j==4:
                print(">>",end="")
            else:
                print("  ",end="")
    print()