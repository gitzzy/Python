for i in range(0, 7):
    for j in range(0, 7):
        if i == 3 or j == 3:
            print("*", end="")
        elif (j > 3 and i == 0) or (i >= 4 and j == 6) or (j < 3 and i == 6) or (i < 3 and j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
