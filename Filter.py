numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#filter
odd_num = list(filter(lambda x:x%2!=0,numbers))
print(odd_num)

#map
sqr = list(map(lambda x:x*x,numbers))
print(sqr)

from functools import reduce
#reduce
factorial = reduce(lambda x,y : x*y,numbers)
print(factorial)

sum = reduce(lambda x,y:x+y,numbers)
print(sum)

def fnc():
    for i in range(0,10):
        print(i)

