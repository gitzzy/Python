for i in range(1,9):
    if i<=3:
        print("* "*i+"  "*(6-(2*i-1))+"* "*(2*i-1)+
              "  "*(6-(2*i-1))+"* "*i)
    else:
        print("* "*13)