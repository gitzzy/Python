val = "Devansh "
val1 = "hello! Sir"
val2 = "123"

# it will print the length of the Variable
print(len(val))

# to find any char
print(val.find("a"))

#Count number of charcter in that String
print(val.count("n"))

#capitalize First Letter
print(val1.capitalize())

print(val.upper())
print(val.lower())

print(val.isdigit())

print(val1.replace("hello","Bye"))

print(val*3)

#Slicing [start:stop:step]

ram = "Jai Shri Ram"
print(ram)
print(ram[0:4])

#Reverse a string in python
print(ram[::-1])

web = "https://aniwave.t0/"
slice = slice(8,-4)
print(web[slice])