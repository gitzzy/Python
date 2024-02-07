#Dictionary
#Very similar to Mapping in java
#ofc Value can be changed
myDict = {0:"A",1:'B'}
print(myDict[0])

myDict[0] = "a"
print(myDict[0])

print("Before delete")
print(myDict)

del myDict[0]
print("After Delete")
print(myDict)

print(myDict.items())
print(myDict.keys())
print(myDict.values())