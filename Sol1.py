#Map

l = [1,2,3,4,5]

sqr = list(map(lambda x:x*x,l))
print(sqr)

#(lambda x:x%2!=0,numbers)
f = list(filter(lambda x:x%2==0,l))

print(f)
from functools import reduce
fac = reduce(lambda x,y:x+y,l)
print(fac)