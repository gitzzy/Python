num = 0
num2 = 1
for i in range(0,5):
    for j in range(0,5):
        num +=1
        if num%2 == 0:
            print("",num2,end="")
            num2 +=1
        else:
            print(" *",end="")
    print()
