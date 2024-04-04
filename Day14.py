for i in range(0,4):
    for k in range(0,3):
        for j in range(0,18):
            if i==0 and j>0+(6*k) and j<5+(6*k) or (j==1+(6*k) or j==4+(6*k)) or (i==3 and j<2+(6*k)) or (i==3 and j>4+(6*k)):
                print("* ",end="")
            else:
                print("  ",end="")

    # for k in range(0,6):
    #     if i==0 and k>0 and k<5 or (k==1 or k==4) or (i==3 and k<2) or (i==3 and k>4):
    #         print("* ",end="")
    #     else:
    #         print("  ",end="")
    # for l in range(0,6):
    #     if i==0 and l>0 and l<5 or (l==1 or l==4) or (i==3 and l<2) or (i==3 and l>4):
    #         print("* ",end="")
    #     else:
    #         print("  ",end="")
    print()