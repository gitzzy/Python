#Arbitrary function
def Arbi(*args):
    for i in args:
        print(i,end=" ")

#Calling
Arbi("Hello",1,2,8,True,3.15)
print()


#Default Arguments
def greet(name='Devansh'):
    print(f"Hello! {name}")

greet('Modi')
greet()

#Keyword arguments
def wish(name , city):
    print(f"Hello {name} from {city}.")
wish(name='Devansh',city='New York')
wish('Amit Malviya','Ayodhya')