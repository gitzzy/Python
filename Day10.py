alpha = 65
iLim = 0
jLim = 0
cyc = 7 

rows, cols = (8, 8)
arr = [[chr(65) for _ in range(cols)] for _ in range(rows)]
arr[0][0] = chr(65)
while True:
    
    if jLim < cyc:
        jLim += 1
    elif iLim < cyc:
        iLim += 1
    else:
        break
    alpha += 1

    if alpha > 90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)

while True:
    if jLim > 0:
        jLim -= 1
    elif iLim >1:
        iLim -= 1
    else:
        break
    alpha +=1

    if alpha >90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)

while True:
    
    if jLim < cyc-1:
        jLim += 1
    elif iLim < cyc-1:
        iLim += 1
    else:
        break
    alpha += 1
    if alpha > 90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)

while True:
    if jLim > 1:
        jLim -= 1
    elif iLim >2:
        iLim -= 1
    else:
        break
    alpha +=1

    if alpha >90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)

while True:
    
    if jLim < cyc-2:
        jLim += 1
    elif iLim < cyc-2:
        iLim += 1
    else:
        break
    alpha += 1
    if alpha > 90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)

while True:
    if jLim > 2:
        jLim -= 1
    elif iLim >3:
        iLim -= 1
    else:
        break
    alpha +=1

    if alpha >90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)

while True:
    
    if jLim < cyc-3:
        jLim += 1
    elif iLim < cyc-3:
        iLim += 1
    else:
        break
    alpha += 1
    if alpha > 90:
        alpha = 65
    arr[iLim][jLim] = chr(alpha)
    arr[4][3] = 'L'

for i in range(0, 8):
    for j in range(0, 8):
        print(arr[i][j], end=" ")
    print()
