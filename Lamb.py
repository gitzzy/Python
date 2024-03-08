def sqr(x):
    return x*x

def add(x,y):
    return x+y

lists = [1,2,3,4,5]

def sqrs(fnc,iter):
    res = []
    for i in iter:
        newI = fnc(i)
        res.append(newI)
    return res

sq = sqrs(lambda x:x**2,lists)
print(sq)

def a(lst,it):
    lst1 =[]
    for i in it:
         itm = lst(i)
         lst1.append(itm)
    return lst1

ress = a(lambda x:x**3,lists)

print(ress)



print(sqr(5))
print(add(5,6))