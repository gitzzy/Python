for i in range(0,7):
    for j in range(0,7):
       res = max(abs(3 -i),abs(3 -j))+1
       print(res,end=" ")
    print()