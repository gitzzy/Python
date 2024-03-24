mon = int(input("Number of Months : "))

num1 = 1000
num2 = 1000
num3 = num1 + num2 # 2
total =2000
if mon>0:
    for i in range(1,mon):
        res = num1 + num2
        total += res
        num1 ,num2 = num2 , res

print(total)