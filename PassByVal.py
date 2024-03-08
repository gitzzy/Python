def fnc(x):
    x = x+10
    print("Inside Function : ",x)

num = 5
print("Raw Data : ",num)
fnc(num)
print("end : ",num)

#pass by ref
lists = ["Hi","Bye"]
def fnc1(x):
    x.append("Boi")
    print("Inside",x)

fnc1(lists)
print("Outside fnc ",lists)