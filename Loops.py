table = int(input("Kiski table likhu : "))
limit = int(input("Kha Tak likhu : "))+1
for i in range(1,limit):
    print(str(table)+" X "+str(i)+" = "+str((i*table)))
print("End")