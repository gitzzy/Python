print("Hello")
myList = [1,2,3,4,5,6,7,8,9]

#filters
def even(myList):
    print(list(filter(lambda x:x%2==0,myList)))

#Will filter the myList and print only the even numbers in list
even(myList)

#Map

def squaring(myList):
    print(list(map(lambda x: x*x,myList)))

#Will square all the iteratives and return the result
squaring(myList)

#reduce() function
from functools import reduce
def ap(myList):
    print(reduce(lambda x,y: x*y,myList))

ap(myList)
#it will reduce the list to one single element in our case we are adding
#all the elements in the list

