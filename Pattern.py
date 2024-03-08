
a = 0
r= int(input("Enter the Size of Pyramid : "))
for j in range(1,r):
    a=(r-1)-j
    print("  "*a,f"* "*(2*j -1))
