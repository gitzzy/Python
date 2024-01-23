import random

a = random.randrange(1,8)
b = random.randrange(1,8)
c = random.randrange(1,8)
res = 7*7*7
print(a,b,c)
if a==b==c==7 :
    print("Congratulations! , you won lottery")
    print("chances are 1/",res)
else :
    print("gambare! gambare!") 
    print("chances are 1/",res)