for i in range(0,5):
    for j in range(0,5):
        if j<4-i:
            print(chr(65+j),end=" ")
        else:
            print(chr(69-i),end=" ")
    print() 