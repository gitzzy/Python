alpha = 65
iLim = 0
jLim = 0
cyc = 7 

rows, cols = (8, 8)
arr = [[chr(65) for _ in range(cols)] for _ in range(rows)]
arr[0][0] = chr(65)

def inc(a):
    global alpha, iLim, jLim
    while True:
        if jLim < cyc-a:
            jLim += 1
        elif iLim < cyc-a:
            iLim += 1
        else:
            break
        alpha += 1

        if alpha > 90:
            alpha = 65
        arr[iLim][jLim] = chr(alpha)

def dec(a,b):
    global alpha, iLim, jLim
    while True:
        if jLim > a:
            jLim -= 1
        elif iLim >b:
            iLim -= 1
        else:
            break
        alpha +=1

        if alpha >90:
            alpha = 65
        arr[iLim][jLim] = chr(alpha)

for i in range(0,4):
    inc(i)
    dec(i,i+1)
for i in range(0, 8):
    for j in range(0, 8):
        print(arr[i][j], end=" ")
    print()