MyList =[1,2,3,4,5,6]

for i in MyList:
    #Reverse Display
    print(MyList[-i])
print("End")

print("Original List : ")
print(MyList[0:6])

#Appending  
print("Appending : ")
MyList.append(7)
print(MyList)

#Extending
print("Extending :")
MyList.extend([0,0])
print(MyList)

#Lengsth of List
print("Length of List :",len(MyList))

# in keyword
print("'in' keyword uses")
print(4 in MyList)
print(9 in MyList)