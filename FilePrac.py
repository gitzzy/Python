

with open("file2.txt",'+a')as file:
    file.write(input("Type : "))
    file.write("\n")

with open("file2.txt",'r')as file:
    print(file.read())