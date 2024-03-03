#Defining function
def fnc():
    print("Hello")

#Funcion calling
fnc()

#Parameter Function
def fnc1(a,b):
    res=a+b
    return res
fnc1(3,3)

#Coustom Parameter
def greet(name, lang="Bonjour"):
    msg = f"{lang} {name}"
    print(msg)

greet("Devansh")
greet("Ram","Jai Shri")
