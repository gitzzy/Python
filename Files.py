while(True):
    print("<-----Dear, Diary----->")
    print()
    print("<-----Options : ----->")
    print("1. Read")
    print("2. Write")
    print("3. Exit")

    print("Choose Option (1/2/3) :")
    opt = int(input())
    if opt == 1:
        with open('file1.txt','r')as file:
            content = file.read()
            print("<----- FIle Content ----->")
            print(content)
            print("<----- END ----->")
            print()
    elif opt == 2:
        with open('file1.txt','a')as file:
            print("Write.... <NOTE : Type 'XIT' to quit>")
            while(True):
                con = input()
                if(con == "XIT"):
                    break
                else:
                    file.write(con+"\n")
                    continue                
    elif opt == 3:
        exit()
    else:
        print("Invalid Option")        

