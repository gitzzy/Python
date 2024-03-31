for i in range(7):
    if i <= 3:
        print("  "*i,(chr(65+i)+" ")*(7-2*i))
    else:
        print("  "*(6-i),(chr(65+i)+" ")*(i-(6-i)+1))
