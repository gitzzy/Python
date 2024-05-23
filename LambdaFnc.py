sqr = lambda x: x*x
res = sqr(6)
print(res)


def squaring(x,y):
    return lambda a:x**y

s=squaring(2,3)
print(s)

def Fnc(fx,val):
    return fx(val)

print(Fnc(lambda x:x*x,3))