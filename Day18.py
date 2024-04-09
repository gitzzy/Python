iLim,jLim,cyc = (0,0,4)
arr = [[chr(65) for _ in range(5)] for _ in range(5)]
arr[0][0] = 25
alpha = 25

def inc(a):
    global alpha, iLim, jLim
    while True:
        if jLim < cyc-a:
            jLim += 1
        elif iLim < cyc-a:
            iLim += 1
        else:
            break
        alpha -= 1
        arr[iLim][jLim] = alpha
    
def dec(a,b):
    global alpha, iLim, jLim
    while True:
        if jLim > a:
            jLim -= 1
        elif iLim >b:
            iLim -= 1
        else:
            break
        alpha -=1
        arr[iLim][jLim] = alpha   

for i in range(0,3):
    inc(i)
    dec(i,i+1)

for i in range(0, 5):
    for j in range(0, 5):
        if int(arr[i][j]) <= 9:
            print(f"0{arr[i][j]}", end=" ")
        else:
            print(arr[i][j],end=" ")
    print()
